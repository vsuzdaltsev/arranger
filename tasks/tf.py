from collections import OrderedDict
import json
import os
import time

from invoke import task
from jinja2 import Environment


CDKTF_CONFIG = "cdktf.json"


def start_delay(action: str, seconds: int, stack: str, cluster_name_alias: str):
    from .helper_functions import log

    if seconds > 0:
        log(
            "warning",
            f">> Waiting for {seconds} seconds before start {action}ing {stack} on {cluster_name_alias}..\n",
        )

        if "prod" in cluster_name_alias:
            log(
                "error",
                ">> !!! ACHTUNG, please be aware that this is a PRODUCTION cluster. !!!",
            )

            log(
                "warning",
                f">> !!! Please press <Ctrl+C> if you want to break execution gracefully.. !!!\n",
            )

        while seconds >= 1:
            seconds -= 1
            log("warning", f">> Remained {seconds} seconds before start..")
            time.sleep(1)
        log(
            "warning",
            f"\n>> Start {action}ing..\n",
        )


def template_env() -> type(Environment):
    """Jinja template environment object."""
    from .helper_functions import ChoiceLoader, FileSystemLoader

    templates = FileSystemLoader("templates")
    loader = ChoiceLoader([templates])
    env = Environment(loader=loader, autoescape=True)
    env.trim_blocks = env.lstrip_blocks = env.rstrip_blocks = True

    return env


def generate_cdktf_json(cluster_name_alias: str, stack: str) -> None:
    """Cdktf json generator."""
    from .helper_functions import (
        CURRENT_TF_PROJECT,
        VALID_CLUSTERS,
        VALID_EKS_STACKS,
        WHERE_CDKTF_WD,
    )

    if cluster_name_alias not in VALID_CLUSTERS:
        raise ValueError(
            f">> 'cluster-name-alias' parameter. Valid: {list(VALID_CLUSTERS.keys())}. Passed: '{cluster_name_alias}'."
        )

    where_template = f"{CDKTF_CONFIG}.j2"
    template = template_env().get_template(where_template)

    if stack not in VALID_EKS_STACKS:
        raise ValueError(
            f">> 'stack' parameter. Allowed: '{VALID_EKS_STACKS}'. Passed: '{stack}'."
        )

    manifest = template.render(cluster_name_alias=cluster_name_alias, stack=stack)
    rendered_manifest = f"{WHERE_CDKTF_WD}/{CURRENT_TF_PROJECT}/{CDKTF_CONFIG}"

    with open(rendered_manifest, mode="w", encoding="utf-8") as service_manifest:
        service_manifest.write(manifest)


@task
def clean_up_cdktf_json(ctx):
    """>> Remove cdktf config."""

    from .helper_functions import CURRENT_TF_PROJECT, WHERE_CDKTF_WD

    where_file = f"{WHERE_CDKTF_WD}/{CURRENT_TF_PROJECT}/{CDKTF_CONFIG}"

    if os.path.exists(where_file):
        os.unlink(where_file)


@task
def infra_action(
    ctx,
    cmd,
    stack=None,
    project=None,
    cluster_name_alias=None,
    parallelism=10,
    log_level="error",
):
    """>> Synthesize Infra stack to generate Terraform code."""
    from arranger_conf.app_conf import AppConf

    from .helper_functions import (
        TERRAFORM_PROJECTS,
        validate_input,
        VALID_EKS_STACKS,
        WHERE_CDKTF_WD,
    )

    validate_input(name="stack", passed=stack, allowed=sorted(VALID_EKS_STACKS))
    validate_input(name="project", allowed=TERRAFORM_PROJECTS, passed=project)
    validate_input(
        name="log_level",
        allowed=["trace", "debug", "info", "warn", "error", "off"],
        passed=log_level,
    )
    validate_input(
        name="cluster_name_alias",
        allowed=list(AppConf.CLUSTERS.keys()),
        passed=cluster_name_alias,
    )

    generate_cdktf_json(cluster_name_alias=cluster_name_alias, stack=stack)
    log_level = f"export TF_LOG={log_level} &&"

    with ctx.cd(f"{WHERE_CDKTF_WD}/{project}"):
        ctx.run(
            f'{log_level} TF_CLI_ARGS_apply="-parallelism={parallelism}" {cmd}',
            pty=True,
        )


@task(post=[clean_up_cdktf_json])
def infra_deploy(
    ctx,
    stack=None,
    project=None,
    cluster_name_alias=None,
    parallelism=10,
    wait_before_start=5,
    log_level="error",
):
    """>> Deploy Infra stack using Terraform."""
    start_delay(
        action="deploy",
        seconds=int(wait_before_start),
        cluster_name_alias=cluster_name_alias,
        stack=stack,
    )
    infra_action(
        ctx,
        cmd=f"rm -rf cdktf.out/stacks/{stack} && cdktf deploy {stack} --auto-approve",
        stack=stack,
        project=project,
        cluster_name_alias=cluster_name_alias,
        parallelism=parallelism,
        log_level=log_level,
    )


@task(post=[clean_up_cdktf_json])
def infra_destroy(
    ctx,
    stack=None,
    project=None,
    cluster_name_alias=None,
    parallelism=10,
    wait_before_start=5,
    log_level="error",
):
    """>> Destroy Infra stack."""
    start_delay(
        action="destroy",
        seconds=int(wait_before_start),
        cluster_name_alias=cluster_name_alias,
        stack=stack,
    )
    infra_action(
        ctx,
        cmd=f"cdktf destroy {stack} --auto-approve",
        stack=stack,
        project=project,
        cluster_name_alias=cluster_name_alias,
        parallelism=parallelism,
        log_level=log_level,
    )


@task(post=[clean_up_cdktf_json])
def infra_diff(
    ctx,
    stack=None,
    project=None,
    cluster_name_alias=None,
    parallelism=10,
    plan_path=None,
    log_level="error",
):
    """>> Show Terraform diff for the Infra stack."""
    from .helper_functions import WHERE_CDKTF_WD

    infra_action(
        ctx,
        cmd=f"cdktf diff {stack}",
        stack=stack,
        project=project,
        cluster_name_alias=cluster_name_alias,
        parallelism=parallelism,
        log_level=log_level,
    )

    if plan_path:
        with ctx.cd(f"{WHERE_CDKTF_WD}/{project}/cdktf.out/stacks/{stack}"):
            ctx.run(f"terraform show -json plan > {plan_path}", pty=True)


@task(post=[clean_up_cdktf_json])
def infra_list(_ctx, project=None, with_descriptions="true", cluster_name_alias=None):
    """>> Show valid Terraform stacks."""
    from arranger_conf.arranger_cdktf_conf import BasicConf

    from .helper_functions import (
        TERRAFORM_PROJECTS,
        TOGGLE,
        validate_input,
        VALID_CLUSTERS,
    )

    validate_input(name="project", passed=project, allowed=TERRAFORM_PROJECTS)
    validate_input(name="with_descriptions", passed=with_descriptions, allowed=TOGGLE)

    if cluster_name_alias:
        validate_input(
            name="cluster_name_alias",
            passed=cluster_name_alias,
            allowed=sorted(VALID_CLUSTERS.keys()),
        )

    def all_stack_names(cluster_name):
        if cluster_name:
            from arranger_conf.arranger_cdktf_conf import TfConf

            cluster_conf = getattr(TfConf, cluster_name.capitalize())
            return getattr(cluster_conf, "ALL_STACKS")
        return list(BasicConf.VALID_STACKS[project].keys())

    def stacks(cluster_name):
        stack_names = all_stack_names(cluster_name=cluster_name)

        if with_descriptions == "true":
            stack_names_with_desc = {}

            for stack_name, metadata in BasicConf.VALID_STACKS[project].items():
                if stack_name in stack_names:
                    stack_names_with_desc.update(
                        {
                            stack_name: {
                                "description": metadata.get("description"),
                                "depends_on": metadata.get("depends_on"),
                            }
                        }
                    )

            return stack_names_with_desc
        return stack_names

    print(json.dumps(stacks(cluster_name=cluster_name_alias)))


@task
def list_clusters(_ctx, verbose="true"):
    """>> Show available clusters."""
    from arranger_conf import AppConf

    from .helper_functions import TOGGLE, validate_input

    validate_input(name="verbose", allowed=TOGGLE, passed=verbose)

    verbose = bool(verbose == "true")

    if verbose:
        return print(json.dumps(OrderedDict(sorted(AppConf.CLUSTERS.items()))))

    return print(json.dumps(sorted(AppConf.CLUSTERS.keys())))


@task
def list_ip_ranges(_ctx, cluster_name_alias=None):
    """
    >> List IP ranges.

    :param cluster_name_alias: Cluster name alias.

    :return: JSON of IP ranges.
    """
    from arranger_automation.validate import ValidateSubnets
    from arranger_conf.app_conf import AppConf
    from arranger_globals import CdktfGlobals

    from .helper_functions import validate_input

    clusters = (
        [cluster_name_alias] if cluster_name_alias else sorted(AppConf.CLUSTERS.keys())
    )

    validate_input(
        name=cluster_name_alias,
        allowed=sorted(AppConf.CLUSTERS.keys()),
        passed=clusters[0],
    )

    ip_ranges = {}
    for cluster in clusters:
        _globals = CdktfGlobals(cluster_name_alias=cluster)

        ip_ranges.update(
            {cluster: ValidateSubnets(ranges=_globals.ip_ranges).validate()}
        )

    print(json.dumps(ip_ranges))

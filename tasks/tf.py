from collections import OrderedDict
import json
import os
import time

from invoke import task
from jinja2 import Environment


CDKTF_CONFIG = "cdktf.json"


def start_delay(action: str, seconds: int, stack: str, tenant: str):
    from .helper_functions import log

    if seconds > 0:
        log(
            "warning",
            f">> Waiting for {seconds} seconds before start {action}ing {stack} in {tenant}..\n",
        )

        if "prod" in tenant:
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


def template_env() -> Environment:
    """Jinja template environment object."""
    from .helper_functions import ChoiceLoader, FileSystemLoader

    templates = FileSystemLoader("templates")
    loader = ChoiceLoader([templates])
    env = Environment(loader=loader, autoescape=True)
    env.trim_blocks = env.lstrip_blocks = env.rstrip_blocks = True

    return env


def generate_cdktf_json(tenant: str, stack: str) -> None:
    """CDKTF json generator."""
    from .helper_functions import (
        CURRENT_TF_PROJECT,
        VALID_TENANTS,
        VALID_EKS_STACKS,
        WHERE_CDKTF_WD,
    )

    if tenant not in VALID_TENANTS:
        raise ValueError(
            f">> 'cluster-name-alias' parameter. Valid: {list(VALID_TENANTS.keys())}. Passed: '{tenant}'."
        )

    where_template = f"{CDKTF_CONFIG}.j2"
    template = template_env().get_template(where_template)

    if stack not in VALID_EKS_STACKS:
        raise ValueError(
            f">> 'stack' parameter. Allowed: '{VALID_EKS_STACKS}'. Passed: '{stack}'."
        )

    manifest = template.render(tenant=tenant, stack=stack)
    rendered_manifest = f"{WHERE_CDKTF_WD}/{CURRENT_TF_PROJECT}/{CDKTF_CONFIG}"

    with open(rendered_manifest, mode="w", encoding="utf-8") as service_manifest:
        service_manifest.write(manifest)


@task
def clean_up_cdktf_json(_ctx):
    """>> Remove CDKTF config."""

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
    tenant=None,
    parallelism=10,
    log_level="error",
):
    """>> Synthesize Infrastructure stack to generate Terraform code."""
    from arranger_conf.arranger_conf import ArrangerConf

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
        name="tenant",
        allowed=list(ArrangerConf.TENANTS.keys()),
        passed=tenant,
    )

    generate_cdktf_json(tenant=tenant, stack=stack)
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
    tenant=None,
    parallelism=10,
    wait_before_start=5,
    log_level="error",
):
    """>> Deploy Infra stack using Terraform."""
    start_delay(
        action="deploy",
        seconds=int(wait_before_start),
        tenant=tenant,
        stack=stack,
    )
    infra_action(
        ctx,
        cmd=f"rm -rf cdktf.out/stacks/{stack} && cdktf deploy {stack} --auto-approve",
        stack=stack,
        project=project,
        tenant=tenant,
        parallelism=parallelism,
        log_level=log_level,
    )


@task(post=[clean_up_cdktf_json])
def infra_destroy(
    ctx,
    stack=None,
    project=None,
    tenant=None,
    parallelism=10,
    wait_before_start=5,
    log_level="error",
):
    """>> Destroy Infra stack."""
    start_delay(
        action="destroy",
        seconds=int(wait_before_start),
        tenant=tenant,
        stack=stack,
    )
    infra_action(
        ctx,
        cmd=f"cdktf destroy {stack} --auto-approve",
        stack=stack,
        project=project,
        tenant=tenant,
        parallelism=parallelism,
        log_level=log_level,
    )


@task(post=[clean_up_cdktf_json])
def infra_diff(
    ctx,
    stack=None,
    project=None,
    tenant=None,
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
        tenant=tenant,
        parallelism=parallelism,
        log_level=log_level,
    )

    if plan_path:
        with ctx.cd(f"{WHERE_CDKTF_WD}/{project}/cdktf.out/stacks/{stack}"):
            ctx.run(f"terraform show -json plan > {plan_path}", pty=True)


@task(post=[clean_up_cdktf_json])
def infra_list(_ctx, project=None, with_descriptions="true", tenant=None):
    """>> Show valid Terraform stacks."""
    from arranger_conf.arranger_cdktf_conf import BasicTfConf

    from .helper_functions import (
        TERRAFORM_PROJECTS,
        TOGGLE,
        validate_input,
        VALID_TENANTS,
    )

    validate_input(name="project", passed=project, allowed=TERRAFORM_PROJECTS)
    validate_input(name="with_descriptions", passed=with_descriptions, allowed=TOGGLE)

    if tenant:
        validate_input(
            name="tenant",
            passed=tenant,
            allowed=sorted(VALID_TENANTS.keys()),
        )

    def all_stack_names(tenant_name):
        if tenant_name:
            from arranger_conf.arranger_cdktf_conf import TfConf

            tenant_conf = getattr(TfConf, tenant_name.capitalize())
            return getattr(tenant_conf, "ALL_STACKS")
        return list(BasicTfConf.VALID_STACKS[project].keys())

    def stacks(tenant_name):
        stack_names = all_stack_names(tenant_name=tenant_name)

        if with_descriptions == "true":
            stack_names_with_desc = {}

            for stack_name, metadata in BasicTfConf.VALID_STACKS[project].items():
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

    print(json.dumps(stacks(tenant_name=tenant)))


@task
def list_tenants(_ctx, verbose="true"):
    """>> Show available tenants."""
    from arranger_conf import ArrangerConf

    from .helper_functions import TOGGLE, validate_input

    validate_input(name="verbose", allowed=TOGGLE, passed=verbose)

    verbose = bool(verbose == "true")

    if verbose:
        return print(json.dumps(OrderedDict(sorted(ArrangerConf.TENANTS.items()))))

    return print(json.dumps(sorted(ArrangerConf.TENANTS.keys())))


@task
def list_ip_ranges(_ctx, tenant=None):
    """
    >> List IP ranges.

    :param tenant: Cluster name alias.

    :return: JSON of IP ranges.
    """
    from arranger_automation.validate import ValidateSubnets
    from arranger_conf.arranger_conf import ArrangerConf
    from arranger_globals import CdktfGlobals

    from .helper_functions import validate_input

    tenants = [tenant] if tenant else sorted(ArrangerConf.TENANTS.keys())

    validate_input(
        name=tenant,
        allowed=sorted(ArrangerConf.TENANTS.keys()),
        passed=tenants[0],
    )

    ip_ranges = {}
    for tenant in tenants:
        _globals = CdktfGlobals(tenant=tenant)

        ip_ranges.update(
            {tenant: ValidateSubnets(ranges=_globals.ip_ranges).validate()}
        )

    print(json.dumps(ip_ranges))

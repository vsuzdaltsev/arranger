import base64
import json
import os
import random
import time

from invoke import task

from .helper_functions import *  # (

# FIXME: add granular imports to respective functions
# AppConf,
# kubeconfig_name,
# KUBERNETES_VERSION,
# log,
# repo_root,
# template_env,
# TOGGLE,
# validate_input,
# VALID_CLUSTERS,
# VALID_ENVIRONMENTS,
# )
from .local import cleanup_repo


def run_kubeconfig_generation(cmd, ctx, where_config):
    import yaml

    result = ctx.run(cmd, hide=True, warn=False)

    if not os.path.exists(where_config):
        raise FileNotFoundError(
            f">> File {where_config} is not generated. Error: {result.stderr}."
        )

    if os.path.exists(where_config):
        with open(where_config, "r") as kubeconfig_file:
            contents = kubeconfig_file.read()

            try:
                config = yaml.safe_load(contents)
                for attr in ["kind", "apiVersion", "clusters"]:
                    config[attr] and log(
                        "debug",
                        f">> Kubeconfig file '{where_config}' contains attribute '{attr}'.",
                    )
            except Exception as err:
                raise RuntimeError(
                    (
                        f">> Generated file {where_config} is not a valid YAML kubeconfig. "
                        f"It doesn't contain attribute '{attr}'."
                    )
                ) from err


@task
def update_kubeconfig_eks(ctx, tenant=None, kubeconfig_file=None, assume_role=None):
    """>> Update kubeconfig for given EKS cluster."""
    if tenant not in VALID_TENANTS:
        raise ValueError(
            (
                f">> Parameter 'cluster_name_alias' must be in {list(VALID_TENANTS.keys())}. "
                f"Given: '{tenant}'."
            )
        )

    def _g():
        from arranger_globals.cdktf_globals import ByTenant

        return ByTenant(tenant=tenant)

    where_config = kubeconfig_file if kubeconfig_file else _g().where_kubeconfig

    log("debug", f">> Config file: {where_config}.")

    assert assume_role in [
        None,
        _g().eks_kubectl_sso_role,
    ], f">> Parameter 'assume_role' can be None or {_g().eks_kubectl_sso_role}. You passed '{assume_role}'."

    def _assume_role_arn():
        if assume_role:
            return f"--role-arn arn:aws:iam::{_g().aws_account_id}:role/{assume_role}"
        return ""

    log("debug", f">> Eks: {_g().cluster_name}.")
    options = (
        f"--name {_g().cluster_name_short} "
        f"--profile {_g().aws_profile} "
        f"--region {_g().aws_region} "
        f"{_assume_role_arn()}"
    )
    log("debug", f">> Options: {options}.")
    cmd = f"export KUBECONFIG={where_config} && aws eks update-kubeconfig {options}"
    log("warning", f">> Execute command: {cmd}.")

    run_kubeconfig_generation(cmd, ctx, where_config)


@task(post=[cleanup_repo])
def generate_k8s_manifests(
    ctx,
    inputs=None,
    environment=None,
    overrides=None,
    patches=None,
    override_image_tag=None,
    file="main.py",
    debug="false",
):
    """
    >> Generate K8s manifest for given service and environment. Universal version.

    :param inputs: List of services.
    :param environment: K8s environment. E.g.: "d1", "dev", "prod".
    :param overrides: [Optional] Overrides for Conf objects. To be passed to the entrypoint.
        Represented by json-like string.
        E.g.:
            '{"K8sConf.Dev1.Identity.IMAGE": "my_image"}'.

    :param patches: [Optional] List of patches to apply to the generated structure. Similar to 'kustomize edit'.
        Represented by json-like string.
        E.g.:
            '[{
                "key": "image",
                "value": "<>.dkr.ecr.eu-west-2.amazonaws.com/identity-service",
                "new_value": "<>.dkr.ecr.eu-west-2.amazonaws.com/identity-service:1.1.1"
            }]'

    :param override_image_tag: [Optional] Add given tag to all the images in the manifest
        (besides excludes listed in the DONT_ADD_OVERRIDE_IMAGE_TAG_FOR constant).
    :param file: Entry point for the generator.
    :param debug: [Optional] Suppress debug output or no. "true" or "false" allowed.
    """
    import yaml
    from arranger_conf.arranger_cdk8s_conf_lib._basic_service import BasicService

    def _g():
        from arranger_globals.basic_arranger_globals import ByEnvironment

        return ByEnvironment(environment=environment)

    DONT_ADD_OVERRIDE_IMAGE_TAG_FOR = [
        # f"public.ecr.aws/docker/library/postgres:alpine{ArrangerConf.DEFAULT_ALPINE_IMAGE}",
        # f"postgres:alpine{ArrangerConf.DEFAULT_ALPINE_IMAGE}",
        # "cassandra",
    ]

    services_list = sorted([srv.strip() for srv in inputs.split(",")])
    for srv in services_list:
        validate_input(
            name="services",
            passed=srv,
            allowed=list(BasicService.valid_services().keys()) + ["all-services"],
        )

    from arranger_automation.parse import PatchK8sManifest, PatchK8sManifestImageTag

    yaml.warnings({"YAMLLoadWarning": False})

    if overrides:
        message_bytes = overrides.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_encoded_overrides = base64_bytes.decode("ascii")
        overrides = base64_encoded_overrides

    if debug not in TOGGLE:
        validate_input(name="debug", passed=debug, allowed=TOGGLE)

    def print_contents(manifest_contents, patches_list, tag):
        if not patches_list and not tag:
            print(manifest_contents)
        else:
            try:
                if patches_list:
                    patches_list = json.loads(patches_list)
                    assert isinstance(patches_list, list)
                    assert all(isinstance(patch, dict) for patch in patches_list)
                else:
                    patches_list = []

            except json.decoder.JSONDecodeError as decode_error:
                log(
                    "error",
                    f">> Wrong patches_list value. Should be parsable to json. Error: {decode_error}.",
                )

            try:
                manifests = list(yaml.load_all(manifest_contents))
                for manifest in manifests:
                    for patch in patches_list:
                        manifest = PatchK8sManifest(struct=manifest, patch=patch).add()

                    manifest = PatchK8sManifestImageTag(
                        struct=manifest,
                        image_tag=tag,
                        excludes=DONT_ADD_OVERRIDE_IMAGE_TAG_FOR,
                    ).add()

                    print("---")
                    print(yaml.dump(manifest))

            except json.decoder.JSONDecodeError as decode_error:
                log(
                    "error",
                    f">> Wrong parameter value. Should be parsable to json. Error: {decode_error}.",
                )

    hide_debug = bool(debug != "true")
    where_cdk8s_scripts = f"{repo_root()}/python3/scripts/arranger_cdk8s"
    template = template_env().get_template("cdk8s.yaml.j2")
    config = template.render(
        inputs=inputs,
        environment=environment,
        kubernetes_version=KUBERNETES_VERSION,
        overrides=overrides,
        file=file,
    )

    with open(
        f"{where_cdk8s_scripts}/cdk8s.yaml", mode="w", encoding="utf-8"
    ) as cdk8s_config:
        cdk8s_config.write(f"{config}\n")

    with ctx.cd(where_cdk8s_scripts):
        result = ctx.run("cdk8s synth", hide=hide_debug, warn=hide_debug)

        if result.exited != 0:
            raise ValueError(
                f">> Generated empty manifest. Run with debug=true for details.\nError: {result.stderr}."
            )

        generated_files = [
            file
            for file in result.stdout.strip().split("\n")
            if "dist/" in file and ".yaml" in file
        ]

        for generated_file in generated_files:
            generated_file = generated_file[4:]
            with open(
                f"{where_cdk8s_scripts}/{generated_file}", mode="r", encoding="utf-8"
            ) as cdk8s_config:

                contents = cdk8s_config.read()
                filename = generated_file.split("/")[-1]
                print(f"---\n# {environment}:{filename}")
                print_contents(
                    manifest_contents=contents,
                    patches_list=patches,
                    tag=override_image_tag,
                )


@task
def generate_arranger_app(
    ctx,
    services=None,
    environment=None,
    overrides=None,
    patches=None,
    debug="false",
    override_image_tag=None,
):
    """>> Generate K8s manifest for the arranger_app with given services list and environment."""
    validate_input(name="environment", passed=environment, allowed=VALID_ENVIRONMENTS)

    generate_k8s_manifests(
        ctx,
        inputs=services,
        environment=environment,
        overrides=overrides,
        patches=patches,
        file="main.py",
        debug=debug,
        override_image_tag=override_image_tag,
    )


@task
def list_services(_ctx, verbose="false", environment=None, serialize="json"):
    """>> List available K8s services."""
    validate_input(name="verbose", passed=verbose, allowed=TOGGLE)
    validate_input(name="serialize", passed=serialize, allowed=("json", "yaml"))

    def struct(serialisation_type):
        if serialisation_type == "yaml":
            import yaml

            return yaml.dump

        return json.dumps

    def valid_services():
        if environment:
            from arranger_globals import ByEnvironment

            return ByEnvironment(environment=environment).all_services

        from arranger_conf.arranger_cdk8s_conf_lib._basic_service import BasicService

        return BasicService.valid_services()

    if verbose == "true":
        return print(struct(serialisation_type=serialize)(valid_services()))

    brief_list = {}
    for srv, metadata in valid_services().items():
        brief_list.update({srv: metadata.get("description")})

    return print(struct(serialisation_type=serialize)(brief_list))

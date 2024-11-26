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
        from arranger_globals.basic_arranger_globals import BySubEnvironment

        return BySubEnvironment(environment=environment)

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


#
#
# @task
# def rollout_restart_deployment(
#     ctx, cluster_name_alias, deployment_name, namespace="eusy"
# ):
#     """>> Rollout-restart given deployment in given K8s cluster."""
#     ctx.run(f"inv k8s.update-kubeconfig-aks --cluster-name-alias {cluster_name_alias}")
#     log(
#         "warning",
#         (
#             f">> Starting deployment '{deployment_name}' rollout "
#             f"in cluster '{cluster_name_alias}', namespace '{namespace}'."
#         ),
#     )
#     ctx.run(
#         f"export KUBECONFIG={kubeconfig_name(cluster_name_alias=cluster_name_alias)} && "
#         f"kubectl -n {namespace} rollout restart deployment/{deployment_name} && "
#         f"kubectl -n {namespace} rollout status  deployments/{deployment_name}"
#     )
#
#
# @task
# def rollout_deployments(ctx, manifests_file, environment):
#     """>> Parse K8s manifest to get a list of deployments and run rollout restart for them."""
#     from threading import Lock
#     from time import gmtime, strftime
#
#     import yaml
#
#     from arranger_automation.slack import AwsCodebuildSlackThread
#     from arranger_automation.threads import Parallel
#     from arranger_globals.basic_arranger_globals import ByEnvironment
#
#     from .docker import build_initiator, codebuild_url
#
#     def deployment_names():
#         with open(manifests_file, mode="r", encoding="utf-8") as file:
#             contents = file.read()
#
#         manifests = list(yaml.load_all(contents, Loader=yaml.SafeLoader))
#
#         deployments = []
#         for manifest in manifests:
#             if manifest and manifest.get("kind") == "Deployment":
#                 deployments.append(manifest.get("metadata", {}).get("name"))
#
#         return deployments
#
#     deployments_to_restart = deployment_names()
#     _globals = ByEnvironment(environment=environment)
#
#     if deployments_to_restart:
#         rollout_cmd = f"kubectl rollout restart -n {environment} deployment {' '.join(deployments_to_restart)}"
#         log("warning", f">> Running '{rollout_cmd}'..")
#
#         ctx.run(rollout_cmd)
#
#         os.environ["MAX_THREADS"] = str(len(deployments_to_restart))
#
#         start_time = time.time()
#
#         initial_message = "\n".join(
#             [
#                 f"Start rollout of {deployments_to_restart} at: {strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime())} (GM)",
#                 f"Environment: {environment}",
#                 f"Build initiator: {build_initiator(_globals=_globals)}",
#             ]
#         )
#
#         thread = AwsCodebuildSlackThread(channel_id=_globals.slack_channel_id)
#         thread.parent_message(initial_message=initial_message)
#
#         @Parallel.each_slice
#         def wait_rollout(deployment_name):
#             _start_time = time.time()
#             random_sleep = random.randint(0, 5)
#             time.sleep(random_sleep)
#             log(
#                 "warning",
#                 f">> Sleeping for {random_sleep} seconds before starting rollout for {deployment_name}..",
#             )
#             log("warning", f">> Start watching '{deployment_name}' rollout status..")
#             cmd = (
#                 f"kubectl rollout status -n {environment} deployments/{deployment_name}"
#             )
#             log("warning", f">> Running '{cmd}'..")
#             result = ctx.run(cmd)
#             log(
#                 "warning", f">> '{deployment_name}' rollout exit code: {result.exited}."
#             )
#
#             if result.stderr:
#                 log(
#                     "warning", f">> '{deployment_name}' rollout stderr {result.stderr}."
#                 )
#
#             log("warning", f">> '{deployment_name}' rollout stdout {result.stdout}.")
#
#             if result.exited != 0:
#                 raise ValueError(
#                     f">> Could not get rollout status of '{deployment_name}'.\nError: {result.stderr}."
#                 )
#
#             mutex.acquire(timeout=300)
#             results.append(result.exited)
#             _end_time = time.time()
#             thread.additional_message(
#                 additional_message=json.dumps(
#                     {
#                         "deployment": f"{deployment_name}",
#                         "result": f"{result.stdout}",
#                         "time_taken": round(_end_time - _start_time),
#                     }
#                 ),
#                 color="green" if result.exited == 0 else "red",
#             )
#             mutex.release()
#
#         mutex = Lock()
#         results = []
#
#         wait_rollout(deployments_to_restart)
#
#         end_time = time.time()
#         time_taken = end_time - start_time
#
#         thread.update_message(
#             update_message=(
#                 f"{initial_message}\n"
#                 f"Codebuild build ID {os.getenv('CODEBUILD_BUILD_ID')}\n"
#                 f"Codebuild build URL: {codebuild_url()}\n"
#                 f"Time taken: {round(time_taken)}s\n"
#             ),
#             color="green" if all(exited == 0 for exited in results) else "red",
#             custom_status="succeeded"
#             if all(exited == 0 for exited in results)
#             else "red",
#         )
#         log("debug", f">> Exit codes for each thread: {results}.")
#         log(
#             "warning",
#             f">> Rollout restart for {deployments_to_restart} has been performed successfully.",
#         )
#
#
# @task
# def list_services(_ctx, verbose="false", environment=None, serialize="json"):
#     """>> List available K8s services."""
#     validate_input(name="verbose", passed=verbose, allowed=TOGGLE)
#     validate_input(name="serialize", passed=serialize, allowed=("json", "yaml"))
#
#     def struct(serialisation_type):
#         if serialisation_type == "yaml":
#             import yaml
#
#             return yaml.dump
#
#         return json.dumps
#
#     def valid_services():
#         if environment:
#             from arranger_globals import ByEnvironment
#
#             return ByEnvironment(environment=environment).all_services
#
#         from arranger_conf.arranger_cdk8s_conf_lib._basic_service import BasicService
#
#         return BasicService.valid_services()
#
#     if verbose == "true":
#         return print(struct(serialisation_type=serialize)(valid_services()))
#
#     brief_list = {}
#     for srv, metadata in valid_services().items():
#         brief_list.update({srv: metadata.get("description")})
#
#     return print(struct(serialisation_type=serialize)(brief_list))
#
#
# @task
# def ldap_objects_from_pod(
#     ctx, cluster_name_alias, print_stdout="true", output_to_file=None
# ):
#     """>> Get ldif backup from running openldap pod."""
#
#     from arranger_automation_aws.sm import SecretsManagerItem
#     from arranger_globals.basic_arranger_globals import ByTenant
#
#     validate_input(name="print_stdout", allowed=("true", "false"), passed=print_stdout)
#
#     _globals = ByTenant(cluster_name_alias=cluster_name_alias)
#     ldap_secret = SecretsManagerItem(
#         secret_name=f"{cluster_name_alias}/ldap_stack", aws_profile=cluster_name_alias
#     ).retrieve()
#
#     domain_1 = _globals.domain.split(".")[-1]
#     domain_2 = _globals.domain.split(".")[-2]
#
#     base_dn = f"dc={domain_2},dc={domain_1}"
#     bind_dn = f"cn={ldap_secret.get('adminUser')},{base_dn}"
#
#     password = ldap_secret.get("adminPassword")
#
#     res = ctx.run(
#         f"export KUBECONFIG={kubeconfig_name(cluster_name_alias=cluster_name_alias)} && "
#         f"kubectl exec -n ldap pod/openldap-stack-ha-0 -c openldap-stack-ha -- "
#         f"ldapsearch -x -D {bind_dn} -w {password} -x -H ldap://{_globals.ldap_base_url}:{_globals.ldap_port} -b {base_dn}",
#         hide=True,
#     )
#     if bool(print_stdout == "true"):
#         print(res.stdout)
#
#     if output_to_file:
#         file = f"{repo_root()}/{output_to_file}"
#
#         if os.path.exists(file):
#             raise FileExistsError(f"File {file} already exists.")
#
#         with open(
#             f"{repo_root()}/{output_to_file}", mode="w", encoding="utf-8"
#         ) as ldif:
#             ldif.write(res.stdout)
#
#
# @task
# def backup_ldif_to_s3(ctx, cluster_name_alias, local_input="false"):
#     """>> Backup LDAP objects for given cluster within the S3 bucket."""
#     from arranger_automation_aws.s3 import S3File
#     from arranger_globals.basic_arranger_globals import ByTenant
#     from arranger_conf.app_conf import AppConf
#
#     validate_input(name="local_input", allowed=("true", "false"), passed=local_input)
#     validate_input(
#         name="cluster_name_alias",
#         allowed=list(AppConf.CLUSTERS.keys()),
#         passed=cluster_name_alias,
#     )
#
#     _globals = ByTenant(cluster_name_alias=cluster_name_alias)
#
#     _file = S3File(
#         bucket_name=f"backup-ldap-{cluster_name_alias}", aws_profile=cluster_name_alias
#     )
#     _file_name = f"{_globals.domain}.backup.ldif"
#
#     if not bool(local_input == "true"):
#         os.path.exists(_file_name) and os.remove(_file_name)
#         ctx.run(
#             f"inv k8s.ldap-objects-from-pod "
#             f"--cluster-name-alias {cluster_name_alias} "
#             f"--output-to-file {_file_name} "
#             f"--print-stdout false"
#         )
#     _file.copy_local_file_to_s3(input_file=_file_name, output_file=_file_name)
#
#
# @task
# def backup_s3_to_ldif(_ctx, cluster_name_alias, version=None, output_file=None):
#     """>> Get LDIF file from S3 bucket and put it to local file."""
#     from arranger_automation_aws.s3 import S3File
#     from arranger_globals.basic_arranger_globals import ByTenant
#     from arranger_conf.app_conf import AppConf
#
#     validate_input(
#         name="cluster_name_alias",
#         allowed=list(AppConf.CLUSTERS.keys()),
#         passed=cluster_name_alias,
#     )
#
#     _globals = ByTenant(cluster_name_alias=cluster_name_alias)
#     _file_name = output_file or _globals.ldap_backup_file
#
#     _file = S3File(
#         bucket_name=f"backup-ldap-{cluster_name_alias}", aws_profile=cluster_name_alias
#     )
#
#     os.path.exists(_file_name) and os.remove(_file_name)
#
#     options = {
#         "input_file": _globals.ldap_backup_file,
#         "output_file": output_file,
#     }
#
#     if version:
#         options.update({"version": version})
#
#     _file.copy_file_from_s3(**options)

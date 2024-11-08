import os
from invoke import task

from .helper_functions import (
    CONTAINER_NAME,
    DOCKER_COMPOSE,
    IN_DOCKER,
    log,
    PYTHON3_PACKAGES,
)


@task
def build_docker_compose(ctx):
    """>> Build the Dockerized environment."""
    log("debug", ">> Build applications...")
    ctx.run(f"{DOCKER_COMPOSE} build")


@task
def exec_container(_ctx, shell="zsh"):
    """>> Enter the Arranger service container shell."""
    available_shells = ["bash", "zsh"]
    log("warning", f">> Entering {CONTAINER_NAME} container's {shell}...")

    if shell not in available_shells:
        raise ValueError(
            f">> Provided shell: '{shell}'. Available shells: '{available_shells}'."
        )

    os.system(f"{DOCKER_COMPOSE} exec {CONTAINER_NAME} {shell}")


@task(post=[exec_container])
def run_docker_compose(ctx):
    """>> Run the Dockerized environment."""
    log(
        "debug",
        ">> Please ensure adding your ssh key to ssh-agent before running the container: eval $(ssh-agent -s).",
    )
    log("debug", f">> Running {CONTAINER_NAME}...")
    ctx.run(f"eval $(ssh-agent -s) >/dev/null; {DOCKER_COMPOSE} up -d")


@task
def stop_docker_compose(ctx, remove_container=True):
    """>> Stop the Dockerized environment."""
    log("debug", f">> Stopping {DOCKER_COMPOSE}...")
    ctx.run(f"{DOCKER_COMPOSE} stop")
    if remove_container:
        ctx.run(f"{DOCKER_COMPOSE} rm -f {CONTAINER_NAME}")


@task
def clean_in_docker(ctx):
    """>> Clean environment from within the dockerized CLI."""
    log("debug", ">> Cleaning environment inside container...")
    ctx.run(f"{IN_DOCKER} inv local.cleanup-repo")


@task
def black(ctx):
    """>> Run autocorrection on Python files (using Black)."""
    cmd = "find . -name \\*\\.py | grep -v '/imports/' | xargs black "
    log("warning", ">> Autocorrect python files according to styleguide.")
    ctx.run(cmd)
    # scripts = "python3/scripts"
    all_dirs = (
        [f"python3/packages/{pkg}" for pkg in PYTHON3_PACKAGES]
        # + [f"{scripts}/arranger_cdk8s"]
        # + [f"{scripts}/arranger_cdktf"]
    )
    sources = (directory for directory in all_dirs)
    for pwd in sources:
        with ctx.cd(pwd):
            log("info", f">> Change working directory to {pwd}.")
            log("info", ">> Autocorrect python files according to the styleguide.")
            ctx.run(cmd)


@task
def clean(ctx, patterns):
    """>> Delete files or folders recursively by pattern."""
    # patterns = (".terraform", "terraform.tfstate", "terraform.tfstate.backup", "backend.tf", "secrets.tfvars.json")
    for pattern in patterns:
        ctx.run(f"find . -name '{pattern}' -exec rm -vrf {{}} +")


@task
def cleanup_repo(ctx):
    """>> Clean the environment from within the Dockerized CLI."""
    log("debug", ">> Remove temporary files")
    to_delete = ["Pipfile*"]
    for microservice in []:
        with ctx.cd(f"{microservice}"):
            log("warning", f">> CD into {microservice}")
            log("warning", f">> Delete patterns: {to_delete}")
            clean(ctx, to_delete)

    find_cmd = "find . -type"
    rm_cmd = 'xargs -0 -I {} /bin/rm -rf "{}"'

    ctx.run(f"{find_cmd} d -name .pytest_cache -print0 | {rm_cmd}")

    for pkg in PYTHON3_PACKAGES:
        ctx.run(f'{find_cmd} d -wholename "*{pkg}/dist" -print0 | {rm_cmd}')
        ctx.run(f'{find_cmd} d -wholename "*{pkg}/build" -print0 | {rm_cmd}')

    ctx.run(f'{find_cmd} d -name "__pycache__" -print0 | {rm_cmd}')
    ctx.run(f'{find_cmd} d -name "*.egg-info*" -print0 | {rm_cmd}')
    ctx.run(f'{find_cmd} d -name "*pdoc" -print0 | {rm_cmd}')
    ctx.run(f'{find_cmd} f -name ".coverage" -print0 | {rm_cmd}')
    ctx.run(f'{find_cmd} d -name "htmlcov" -print0 | {rm_cmd}')

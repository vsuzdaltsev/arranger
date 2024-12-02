"""Arranger Automation CLI."""

import glob
from logging import Logger
import os
from typing import Any, Iterable

from jinja2 import ChoiceLoader, Environment, FileSystemLoader
import yaml

# TODO: currently this is the only project, because of flat structure of TF stack libs

try:
    from arranger_conf import ArrangerConf
    from arranger_conf.arranger_cdktf_conf import BasicTfConf
    from arranger_conf import K8sConf

    KUBERNETES_VERSION = ArrangerConf.CDK8S_KUBERNETES_VERSION
    VALID_TENANTS = ArrangerConf.TENANTS
    VALID_EKS_STACKS = BasicTfConf.VALID_STACKS
    VALID_ENVIRONMENTS = sorted(env.lower() for env in K8sConf.ALL_ENVIRONMENTS)
except BaseException as warn:
    msg = (
        ">> WARNING: Not all modules were properly loaded.\n"
        "This is a workaround for initial run of invoke task. No worries.\n"
        f"Error is: {warn}."
        "There are two options for using the bunch of the arranger_automation invoke tasks:\n"
        "1. Build CLI image <inv local.container.build; inv local.container.run>\n"
        "or"
        "2. Build and install arranger_automation packages <inv python3.build-and-install>.\n"
    )
    print(msg)

with open("./docker-compose.yml", "r") as file:
    docker_compose_data = yaml.safe_load(file)

CONTAINER_NAME = list(docker_compose_data["services"].keys())[0]
DOCKER_COMPOSE = "docker-compose -f docker-compose.yml"
IN_DOCKER = f"{DOCKER_COMPOSE} exec -T {CONTAINER_NAME} pipenv run"
PYTHON3_PACKAGES = [
    pkg_home.split("/")[-1] for pkg_home in glob.glob("python3/packages/*")
]
RENDERED_TEMPLATES = "rendered_templates"
TOGGLE = ("true", "false")
WHERE_CDKTF_WD = "python3/scripts/arranger_cdktf"


def validate_input(
    name: str, passed: Any, allowed: Iterable, input_name: str = "input"
):
    fail_message = f">> Validate {input_name} '{name}'. Passed: '{passed}'. Allowed: should be in {allowed}."

    if isinstance(allowed, dict):
        allowed = list(allowed.keys())

    if isinstance(passed, str):
        assert passed in allowed, fail_message

    if passed is None:
        raise ValueError(fail_message)

    if isinstance(passed, list):
        for elem in passed:
            assert elem in allowed, fail_message


def repo_root() -> str:
    # TODO: refactor me please
    """Current repo root directory."""
    return os.path.dirname(os.path.abspath(__file__)).replace("/tasks", "")


def log(severity: str, message: str) -> Logger.__getattribute__:
    """Logger wrapper."""
    Logger(name="__name__").__getattribute__(severity)(message)


def validate_package_name(package: str) -> None:
    """Validate packages name."""
    if package not in PYTHON3_PACKAGES:
        raise ValueError(
            f"'package' parameter. Passed: '{package}'. Allowed: one of '{PYTHON3_PACKAGES}'."
        )


def template_env() -> Environment:
    """Jinja template environment object."""
    templates = FileSystemLoader("templates")
    loader = ChoiceLoader([templates])
    env = Environment(loader=loader, autoescape=True)
    env.trim_blocks = env.lstrip_blocks = env.rstrip_blocks = True

    return env

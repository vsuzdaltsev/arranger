import glob
from typing import List

from invoke import task

from .helper_functions import PYTHON3_PACKAGES, repo_root, validate_package_name
from .local import cleanup_repo


@task
def build(ctx, package):
    """>> Build the specified Python package."""
    validate_package_name(package=package)

    with ctx.cd(f"{repo_root()}/python3/packages/{package}"):
        ctx.run("python3 setup.py sdist bdist_wheel")


@task
def install(ctx, package):
    """>> Install the specified Python package."""
    validate_package_name(package=package)

    archive = glob.glob(f"{repo_root()}/python3/packages/{package}/dist/*.tar.gz")[0]
    ctx.run(f"python3 -m pip install {archive}")


@task(pre=[cleanup_repo])
def build_and_install(ctx, packages="all-packages"):
    """>> Build the specified Python package, install it, and clean up the repository."""

    def list_packages(packages_string: str) -> List[str]:
        if packages_string == "all-packages":
            return PYTHON3_PACKAGES

        packages_list = []
        for item in packages_string.split(","):
            item = item.strip()
            validate_package_name(package=item)
            packages_list.append(item)
        return packages_list

    for package in list_packages(packages_string=packages):
        build(ctx, package=package)
        install(ctx, package=package)
        cleanup_repo(ctx)

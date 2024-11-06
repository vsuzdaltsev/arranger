import os
from typing import List

from invoke import task

from .helper_functions import log, PYTHON3_PACKAGES, repo_root


@task
def python(ctx, packages="all-packages"):
    """>> Run specs for given Python package."""

    assert (
        os.getcwd() == repo_root()
    ), f">> The invoke task should be executed in {repo_root()}."

    def packages_to_process() -> List[str]:
        if packages == "all-packages":
            return PYTHON3_PACKAGES

        if packages:
            return sorted(p.strip() for p in packages.split(","))

    def package_dir(name):
        return f"{repo_root()}/python3/packages/{name}/{name}"

    def specs_exist(package_name):
        return all(
            os.path.exists(f"{package_dir(name=package_name)}/{e}")
            for e in ["tests", "pytest.ini"]
        )

    for package in packages_to_process():
        try:
            if specs_exist(package_name=package):
                os.chdir(f"{package_dir(name=package)}")
                ctx.run("pytest --tb=auto --showlocals", pty=True)
                # ctx.run(f"pytest -n {multiprocessing.cpu_count()}")
            else:
                log(
                    "warning",
                    f">> Seems like no tests has been created for package '{package}'.",
                )
        finally:
            os.chdir(repo_root())

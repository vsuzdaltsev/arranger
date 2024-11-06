import inspect

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

from .local import (
    black,
    build_docker_compose,
    clean_in_docker,
    cleanup_repo,
    exec_container,
    run_docker_compose,
    stop_docker_compose,
)
from .python import build, build_and_install, install
from .spec import python

from invoke import Collection


ns = Collection()

cdktf = Collection("tf")
cdk8s = Collection("k8s")
codebuild = Collection("codebuild")
container = Collection("container")
docker = Collection("docker")
arranger_app = Collection("arranger_app")
hc_vault = Collection("hc_vault")
local = Collection("local")
python3 = Collection("python3")
secrets = Collection("secrets")
services = Collection("services")
spec = Collection("spec")

cdk8s.add_collection(arranger_app)

local.add_collection(container)

secrets.add_collection(hc_vault)
hc_vault.add_collection(services)

ns.add_collection(cdktf)
ns.add_collection(cdk8s)
ns.add_collection(codebuild)
ns.add_collection(docker)
ns.add_collection(local)
ns.add_collection(python3)
ns.add_collection(secrets)
ns.add_collection(spec)

container.add_task(build_docker_compose, "build")
container.add_task(clean_in_docker, "clean_repo")
container.add_task(exec_container, "enter")
container.add_task(run_docker_compose, "run")
container.add_task(stop_docker_compose, "stop")

local.add_task(black, "autocorrect_black")
local.add_task(cleanup_repo)

python3.add_task(build)
python3.add_task(build_and_install)
python3.add_task(install)

spec.add_task(python, "python")

from invoke import Collection

from .k8s import update_kubeconfig_eks, generate_arranger_app, list_services
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
from .tf import (
    infra_deploy,
    infra_destroy,
    infra_diff,
    infra_list,
    list_ip_ranges,
    list_tenants,
)


ns = Collection()

cdktf = Collection("tf")
cdk8s = Collection("k8s")
container = Collection("container")
arranger_app = Collection("arranger_app")
local = Collection("local")
python3 = Collection("python3")
spec = Collection("spec")

cdktf.add_task(infra_deploy, "deploy")
cdktf.add_task(infra_destroy, "destroy")
cdktf.add_task(infra_diff, "diff")
cdktf.add_task(infra_list, "list_stacks")
cdktf.add_task(list_tenants)
cdktf.add_task(list_ip_ranges)

cdk8s.add_collection(arranger_app)

local.add_collection(container)

ns.add_collection(cdktf)
ns.add_collection(cdk8s)
ns.add_collection(local)
ns.add_collection(python3)
ns.add_collection(spec)

cdk8s.add_task(list_services)
cdk8s.add_task(update_kubeconfig_eks)

arranger_app.add_task(generate_arranger_app, "generate")


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

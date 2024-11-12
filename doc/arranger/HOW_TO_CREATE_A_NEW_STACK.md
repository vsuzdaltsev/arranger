# How to create a new Infrastructure Stack using CDKTF and Arranger

## Create Stack library:

```shell
$ vim /packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/test_vpc_stack.py
```   

<br>

## Add the new module to the import section of the `arranger_cdktf` package:

in `python3/packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/__init__.py` add

```python
from .test_vpc_stack import *
```

<br>

## Add the Stack section to the VALID_STACKS constant:

in `/packages/arranger_conf/arranger_conf/arranger_cdktf_conf.py`

```python
VALID_STACKS = {
    "tf": {
        "test-vpc-stack": {
            "class_name": "TestVpcStack",
            "description": "Test Terraform stack.",
            "depends_on": [],
        },
    }
}
```

<br>

## Add Stack name to the ALL_STACKS constant for the proper Tenant(s):

in `/packages/arranger_conf/arranger_conf/arranger_cdktf_conf.py`

```python
class TfConf:
    class Development1(BasicConf):
        ALL_STACKS = ["test-vpc-stack"]
```

<br>

## Enter the Arranger container:

```shell
$ inv local.container.run
```

<br>

## Check Terraform diff:

```shell
(arranger) root@cli# inv tf.diff --project tf --tenant development1 --stack test-vpc-stack
```

<br>

## Deploy Terraform Stack:

```shell
(arranger) root@cli# inv tf.deloy --project tf --tenant development1 --stack test-vpc-stack
```

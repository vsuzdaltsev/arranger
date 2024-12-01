# How to create a new Infrastructure Stack using CDKTF and Arranger

## Create a Stack library:

create corresponding stack library file[_demo_iam_user_stack.py](../../python3/packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/_demo_iam_user_stack.py)

<br>

## Add the new module to the import section of the `arranger_cdktf` package:

in [arranger_conf package init file](../../python3/packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/__init__.py) add import line

```python
from ._demo_iam_user_stack.py import *
```

<br>

## Add the Stack section to the VALID_STACKS constant:

in [arranger_cdktf_basic_conf.py](../../python3/packages/arranger_conf/arranger_conf/basic_cdktf_conf/arranger_cdktf_basic_conf.py)

```python
VALID_STACKS = {
    "tf": {
        "demo-iam-user-stack": {
            "class_name": "DemoIamUserStack",
            "description": "Test Terraform stack to create AWS IAM user.",
            "depends_on": [],
        },
    }
}
```

<br>

## Add Stack name to the ALL_STACKS constant for the proper Tenant(s):

in [arranger_cdktf_basic_conf.py](../../python3/packages/arranger_conf/arranger_conf/arranger_cdktf_conf.py)

```python
class TfConf:
    class Development1(BasicConf):
        ALL_STACKS = ["demo-iam-user-stack"]
```

<br>

## Authorize you Terraform providers if needed:

[How to authorize you Arranger](AUTHORIZATION.md)

<br>

## Enter the Arranger container:

```shell
$ inv local.container.run
```

<br>

## Check Terraform diff:

```shell
(arranger) root@cli# inv tf.diff --project tf --tenant development1 --stack demo-iam-user-stack
```

<br>

## Deploy Terraform Stack:

```shell
(arranger) root@cli# inv tf.deloy --project tf --tenant development1 --stack demo-iam-user-stack
```

<br>

## Destroy Terraform Stack:

```shell
(arranger) root@cli# inv tf.destroy --project tf --tenant development1 --stack demo-iam-user-stack
```
<br>

## NB: Under the hood, an AWS Terraform Backend (for keeping state) will be created in S3, along with a Lock in DynamoDB table.

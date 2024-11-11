# How to create a new Infrastructure Stack using CDKTF and Arranger

1. __Create Stack library:__
    ```shell
    $ vim /packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/test_vpc_stack.py
    ```
2. __Add the new module to the import section of the `arranger_cdktf` package:__
    
    in `python3/packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/__init__.py` add

    ```python
    from .test_vpc_stack import *
    ```
3. __Add the Stack section to the VALID_STACKS constant:__

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
4. __Add Stack name to the ALL_STACKS constant for the proper Tenant(s):__

    in `/packages/arranger_conf/arranger_conf/arranger_cdktf_conf.py`

    ```python
    class TfConf:
        class Development1(BasicConf):
            ALL_STACKS = ["test-vpc-stack"]
    ```
5. __Check Terraform diff:__
    ```shell
    (arranger) root@cli# inv tf.diff -p tf --tenant development1 --stack test-vpc-stack
    ```
6. __Deploy Terraform Stack:__
    ```shell
    (arranger) root@cli# inv tf.deloy -p tf --tenant development1 --stack test-vpc-stack
    ```
[[_TOC_]]

# Arranger CLI FAQ

## About this guide

## Contents

## Introduction

### Entities

* What is `sub-environment`?
* What is `cluster`?
* What is `tenant`?
* What's the difference between them?

- `Environment` is an instance of the Product in the scope of `Project` (examples: Local, Dev, Prod, etc).
- `Cluster` is the name of the K8s (Azure AKS in current setup) cluster.
- `Tenant` is the short name for the given `cluster` along with the supporting resources.

In most cases, the sub-environment is the same as the tenant, as their clusters contain only one instance of the
application. The exception is the multi environment clusters, specifically `development1`, which have multiple environment
names (also referred to as sub-environments). All commands mentioned here and below should be executed within the
`arranger` container (refer to the appropriate section of this guide).

### How to install Arranger?

[There is special section describing it.](PREPARE_ENVIRONMENT.md)

* To see the list of existing `tenants` (along with sub-environments) run:

```shell
root@cli# inv tf.list-tenants --verbose false | jq
```

<details>
  <summary>List clusters example output</summary>

```json
[
  "development1",
  "local",
  "staging1"
]
```

</details>

### How to add Terraform provider

1. Create a file `cdktf.json` in the project root

   ```json
   {  
      "language": "python",
      "app": "export CHECKPOINT_DISABLE=true && python main.py",
      "terraformProviders": [
          {
              "name": "local",
              "source": "hashicorp/local",
              "version": "2.4.0"
          }
      ],
      "terraformModules": [],
      "codeMakerOutput": "importz",
      "projectId": "a2eadd6a-eda8-4862-b43d-6d821eeddb58"
   }
   ```

2. In the Docker container run
   ```shell
   $ cdktf get
   ```

3. Copy downloaded folder(s)
   ```shell
   $ cp -r  importz/local python3/packages/arranger_cdktf/arranger_cdktf/imports/
   ```

4. Add the provider name to `python3/packages/arranger_cdktf/arranger_cdktf/imports/__init__.py`


5. Run
   ```shell
   $ inv python3.build-and-install -p arranger_cdktf
   ```

6. Add to `python3/packages/arranger_globals/arranger_globals/cdktf_globals.py`

   ```python
   def local_provider(self, scope) -> Any:
        from arranger_cdktf.imports.local.provider import LocalProvider

        return LocalProvider(scope=scope, id="local-provider")
   ```

7. Run
   ```shell
   $ inv python3.build-and-install -p arranger_globals
   ```

### How to generate Terraform code?

1. Run `tf.diff`
   ```shell
   # example 
   $ inv tf.list-stacks -p tf --with-descriptions false | jq
   $ inv tf.diff --cluster-name-alias development1 --stack vpc-stack --project tf   
   ```
2. The spec will be generated into: `python3/scripts/arranger_cdktf/tf/cdktf.out/stacks/$YOUR_STACK_NAME/cdk.tf.json`

## How to add a new stack

1. Create a file: `python3/packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/new_stack.py`
2. Add the stack here: `python3/packages/arranger_conf/arranger_conf/arranger_cdktf_conf.py`
    - class BasicConf -> VALID_STACKS
    - class class Development1(BasicConf) -> ALL_STACKS
    - class Local(BasicConf): -> ALL_STACKS
3. Add the stack here: `python3/packages/arranger_cdktf/arranger_cdktf/tf/arranger_terraform_stacks/__init__.py`

## How to delete Terraform cache:

   ```shell
   $ rm -fr python3/scripts/arranger_cdktf/tf/cdktf.out/stacks/<ecr>-stack
   ```

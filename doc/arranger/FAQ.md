# Arranger CLI FAQ

## About this guide

## Contents

## Introduction

<br>

### Entities

* What is `tenant`?
* What is `environment (sub-environment)`?
* What is `cluster`?
* What's the difference between them?

- `tenant` is an set of isolated Infrastructure resources. Usually (but not necessarily) tenant refers to a separate
  Cloud account. Each `tenant` operates independently, usually within a shared
  infrastructure, but their data and applications remain isolated from those of other `tenants`. Prod isolated from
  Staging, Dev etc. These are examples of `tenants`.
- `environment` aka `sub-environment` is a namespace within K8s cluster.
- `cluster` is an instance of K8s cluster for specific `tenant`.

In most cases, the `environment` has the same name as the appropriate `tenant` for the cases when we have only one
instance of an application
within the K8s cluster (like production etc.). The exception is the multi environment clusters, specifically
`development1`, which consists of multiple
environments (sub-environments) with reusable Infrastructure parts.

NB: All commands mentioned here and below should be executed within the `arranger` container (refer to the appropriate
section of this guide).

* To see the list of existing `tenants` along with `environments` (`sub-environments`) run:

```shell
root@cli# inv tf.list-tenants --verbose true | jq
>>
{
  "development1": { # tenant name
    "aws_account_id": "<>",
    "aws_region": "eu-west-2",
    "cluster_name": "arn:aws:eks:<>>:<>:cluster/development1", # cluster
    "aws_profile": "development1",
    "context": "",
    "description": "Development account #1.",
  "sub_environments": [ # environments (sub-environments)
    "d1",
    "d2",
    "d3",
    "d4",
    ...
    "d19"
  ],
    "domain": "development1.io",
    "cloud_attributes": {
    "cloud": "aws",
    "tags": {}
  }
},
  "local": {
    "cluster_name": "local-k8s"
  },
  "staging1": {
    "cluster_name": "local-k8s"
  }
}
```

<br>

### How to install Arranger?

[There is special section describing it.](PREPARE_ENVIRONMENT.md)

<br>

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

<br>

### How to generate Terraform code?

1. Run `tf.diff`
   ```shell
   # example 
   $ inv tf.list-stacks -p tf --with-descriptions false | jq
   $ inv tf.diff --tenant development1 --stack vpc-stack --project tf   
   ```
2. The spec will be generated into: `python3/scripts/arranger_cdktf/tf/cdktf.out/stacks/$YOUR_STACK_NAME/cdk.tf.json`

<br>

### How to add a new stack

[There is special section for this.](HOW_TO_CREATE_A_NEW_STACK.md)

<br>

### How to delete Terraform cache:

   ```shell
   $ rm -fr python3/scripts/arranger_cdktf/tf/cdktf.out/stacks/<ecr>-stack
   ```

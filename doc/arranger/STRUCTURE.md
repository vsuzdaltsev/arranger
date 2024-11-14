# Arranger consists of the following parts:

1. `Dockerfile` & `docker-compose.yml` to build and run Arranger CLI

2. `python3/packages` - [Python code compiled into several packages](../../python3/packages/README.md)

    * arranger_automation

      Common automation libraries

    * arranger_automation_aws

      AWS automation libraries

    * arranger_cdktf

      Python CDKTF providers and Infra stacks

    * arranger_conf

      Configuration

    * arranger_globals

      Middleware


4. `python3/scripts` - various helper scripts, including main.py files for running CDK operations

5. `templates` - various templates

6. `tasks` - PyInvoke tasks to organize Arranger CLI
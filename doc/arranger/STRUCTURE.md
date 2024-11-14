# Arranger consists of the following parts:

1. `Dockerfile` & `docker-compose.yml` to build and run `Arranger` CLI

1. `python3/packages`:

    * arranger_automation

      Common automation libraries
      
    </br>
   
    * arranger_automation_aws

      AWS automation libraries

    </br>

    * arranger_cdktf

      Python CDKTF providers and Infra stacks

    </br>

    * arranger_conf

      Configuration

    </br>

    * arranger_globals

      Middleware

    </br>

1. `python3/scripts` - various helper scripts, including main.py files for running CDK operations

1. `templates` - various templates

1. `tasks` - PyInvoke tasks to organize Arranger CLI
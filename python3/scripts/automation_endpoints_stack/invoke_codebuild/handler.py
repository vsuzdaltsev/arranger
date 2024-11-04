import json
import os
from logging import Logger

import boto3


def sts_creds(cluster_name_alias):
    if cluster_name_alias == os.getenv("ORCHESTRA_ACCOUNT"):
        return {
            "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
            "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "aws_session_token": os.getenv("AWS_SESSION_TOKEN"),
        }

    session = boto3.session.Session()
    client = session.client("sts")
    sts_credentials = client.assume_role(
        RoleArn=json.loads(os.getenv("STS_ASSUME_ROLES"))[cluster_name_alias],
        RoleSessionName=f"automation-endpoints-session-{cluster_name_alias}",
        DurationSeconds=3600,
    )["Credentials"]

    return {
        "aws_access_key_id": sts_credentials["AccessKeyId"],
        "aws_secret_access_key": sts_credentials["SecretAccessKey"],
        "aws_session_token": sts_credentials["SessionToken"],
    }


def invoke_codebuild(event, _context):
    def log(severity: str, message: str):
        Logger(name="__name__").__getattribute__(severity)(message)

    codebuild_project_name = event.get("pathParameters", {}).get(
        "codebuild_project_name"
    )
    cluster_name_alias = event.get("path").split("_")[-1]
    creds = sts_creds(cluster_name_alias=cluster_name_alias)
    session = boto3.Session(
        aws_access_key_id=creds["aws_access_key_id"],
        aws_secret_access_key=creds["aws_secret_access_key"],
        aws_session_token=creds["aws_session_token"],
    )
    log(severity="debug", message=f">> Event: {type(event)}.")

    input_vars = json.loads(event.get("body", ""))

    def env_vars_override():
        aggr = []
        for input_var in input_vars:
            aggr.append(
                {
                    "name": input_var,
                    "value": input_vars[input_var],
                    "type": "PLAINTEXT",
                }
            )
        return aggr

    def source_version_override():
        if [
            env.get("value")
            for env in env_vars_override()
            if env["name"] == "source_version"
        ]:
            return [
                env.get("value")
                for env in env_vars_override()
                if env["name"] == "source_version"
            ][0]

        return None

    def invoke():
        log(severity="debug", message=f">> Event: {event}\nContext: {_context}.")
        log(
            severity="debug",
            message=f">> Environment variables override: {env_vars_override()}.",
        )

        build_params = {
            "projectName": codebuild_project_name,
            "environmentVariablesOverride": env_vars_override(),
        }

        if source_version_override():
            build_params.update({"sourceVersion": source_version_override()})

        try:
            c = session.client("codebuild")
            response = c.start_build(**build_params)
            return response, None
        except BaseException as err:
            return None, f"{err}"

    result, error = invoke()
    # codebuild_build_id = json.loads(json.dumps(result.get("build", {}).get("id"), default=str))
    response_body = {
        # "input": event,
        "result": json.loads(json.dumps(result.get("build"), default=str)),
        "error": json.dumps(error),
        # "status_url": f"{os.getenv('STATUS_BASE_URL')}/{codebuild_build_id}",
    }

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(response_body),
    }

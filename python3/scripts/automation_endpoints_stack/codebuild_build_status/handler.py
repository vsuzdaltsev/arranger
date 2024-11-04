import json
import os
from typing import Dict

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


def codebuild_build_status(event, _context):
    codebuild_build_id = event.get("pathParameters", {}).get("codebuild_build_id")
    cluster_name_alias = codebuild_build_id.split(":")[0].split("_")[-1]
    creds = sts_creds(cluster_name_alias=cluster_name_alias)
    session = boto3.Session(
        aws_access_key_id=creds["aws_access_key_id"],
        aws_secret_access_key=creds["aws_secret_access_key"],
        aws_session_token=creds["aws_session_token"],
    )

    def _get_status() -> Dict[str, str]:
        try:
            codebuild = session.client("codebuild")
            response = codebuild.batch_get_builds(ids=[codebuild_build_id])

            if "builds" in response and len(response["builds"]) > 0:
                build_status = response["builds"][0]["buildStatus"]
                return {"buildStatus": build_status}
            else:
                return {"buildStatus": "Build not found"}
        except Exception as e:
            return {"Error": f"{e}"}

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(_get_status()),
    }

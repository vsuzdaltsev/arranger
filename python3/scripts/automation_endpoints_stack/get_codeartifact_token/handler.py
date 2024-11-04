import json
from logging import Logger

import boto3


def get_codeartifact_token(event, _context):
    """
    Payload example:
        curl -X GET -v -H "x-api-key: {api_access_key}" https://{endpoint_url}/v1/automation/get_codeartifact_token/{cluster_name_alias} |jq
    """
    domain = event.get("pathParameters", {}).get("domain")

    def log(severity, message):
        import logging
        import os

        logging.basicConfig(
            level=getattr(logging, os.getenv("LOG_LEVEL") or "ERROR"),
            format="%(levelname)s - %(asctime)s UTC - %(name)s - %(message)s",
        )
        Logger(name="__name__").__getattribute__(severity)(message)

    def issue_token():
        log("error", f">> Event: {event}\nContext: {_context}.")
        log("error", f">> Domain: {domain}.")

        try:
            ca = boto3.client("codeartifact")
            response = ca.get_authorization_token(domain=domain)

            return response.get("authorizationToken"), response.get("expiration"), None
        except BaseException as err:
            return None, None, f"{err}"

    token, expiration, error = issue_token()

    response_body = {
        "codeartifact_token": token,
        "expires": str(expiration),
        "error": error,
        # "_context": f"{_context.__dict__}",
        # "event": f"{event}"
    }

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(response_body),
    }

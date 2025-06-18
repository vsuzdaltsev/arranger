import json
from typing import Any, Dict

from cdktf import TerraformOutput, TerraformResourceLifecycle

from arranger_cdktf.imports.archive.data_archive_file import DataArchiveFile
from arranger_cdktf.imports.aws.api_gateway_api_key import ApiGatewayApiKey
from arranger_cdktf.imports.aws.api_gateway_deployment import ApiGatewayDeployment
from arranger_cdktf.imports.aws.api_gateway_integration import ApiGatewayIntegration
from arranger_cdktf.imports.aws.api_gateway_method import ApiGatewayMethod
from arranger_cdktf.imports.aws.api_gateway_resource import ApiGatewayResource
from arranger_cdktf.imports.aws.api_gateway_rest_api import (
    ApiGatewayRestApi,
    ApiGatewayRestApiEndpointConfiguration,
)
from arranger_cdktf.imports.aws.api_gateway_stage import (
    ApiGatewayStage,
)
from arranger_cdktf.imports.aws.api_gateway_usage_plan import (
    ApiGatewayUsagePlan,
    ApiGatewayUsagePlanApiStages,
)
from arranger_cdktf.imports.aws.api_gateway_usage_plan_key import (
    ApiGatewayUsagePlanKey,
)
from arranger_cdktf.imports.aws.iam_role import IamRole, IamRoleInlinePolicy
from arranger_cdktf.imports.aws.lambda_function import (
    LambdaFunction,
    LambdaFunctionEnvironment,
)
from arranger_cdktf.imports.aws.lambda_permission import LambdaPermission
from arranger_conf import ArrangerConf
from arranger_conf.arranger_cdktf_conf import TfConf

from .basic_stack import AwsBasicStack, Construct


class AutomationEndpointsStack(AwsBasicStack):
    STAGE_NAME = "v1"
    LAMBDA_TIMEOUT = 10

    @property
    def sts_assume_roles(self) -> Dict[str, Dict]:
        from arranger_conf.arranger_conf import ArrangerConf

        roles_env_vars = {"STS_ASSUME_ROLES": {}}

        for tenant in ArrangerConf.SUBORDINATE_ACCOUNTS:
            account_id = ArrangerConf.TENANTS[self.globals.tenant]["aws_account_id"]
            role_name = f"trust-orchestrating-account-iam-role-{tenant}"

            roles_env_vars["STS_ASSUME_ROLES"].update(
                {tenant: f"arn:aws:iam::{account_id}:role/{role_name}"}
            )

        _struct = roles_env_vars["STS_ASSUME_ROLES"]
        _json = json.dumps(_struct)
        roles_env_vars["STS_ASSUME_ROLES"] = _json

        self.log.debug(f">> STS_ASSUME_ROLES environment variable: {roles_env_vars}.")

        return roles_env_vars

    @property
    def orchestra_account(self) -> Dict[str, str]:
        from arranger_conf.arranger_conf import ArrangerConf

        return {"HEAD_ACCOUNT": ArrangerConf.HEAD_ACCOUNT}

    @property
    def slack_signing_secret(self) -> Dict[str, str]:
        return {
            "SLACK_SIGNING_SECRET": self.globals.aws_sm_secret(
                secret_name=f"{self.orchestra_account['HEAD_ACCOUNT']}/slack"
            )["arranger_notification_bot_signing_secret"]
        }

    @property
    def slack_signing_secret_og(self) -> Dict[str, str]:
        return {
            "SLACK_SIGNING_SECRET_OG": self.globals.aws_sm_secret(
                secret_name=f"{self.orchestra_account['HEAD_ACCOUNT']}/slack"
            )["arranger_notification_bot_signing_secret_og"]
        }

    @property
    def ci_job_token(self) -> Dict[str, str]:
        return {
            "CI_JOB_TOKEN": self.globals.aws_sm_secret(
                secret_name=f"{self.orchestra_account['HEAD_ACCOUNT']}/codebuild"
            )["CI_JOB_TOKEN"]
        }

    @property
    def _name_prefix(self) -> str:
        return "automation-endpoints"

    def _zip_file_name(self, prefix: str) -> str:
        return self._name(object_type=f"{prefix}-zip-file-name")

    def __init__(self, scope: Construct, ns: str, config: TfConf):
        super().__init__(scope, ns, config=config)

        self.aws_provider = self.globals.automation(scope=self)
        self.archive_provider = self.globals.archive_provider(scope=self)

        self.rest_api = self._rest_api()

        # INVOKE CODEBUILD lambda
        self.invoke_codebuild_handler_zip = self._invoke_codebuild_handler_zip()
        self.invoke_codebuild_lambda_execution_role = (
            self._invoke_codebuild_lambda_execution_role()
        )
        self.invoke_codebuild_lambda = self._invoke_codebuild_lambda()
        self.invoke_codebuild_lambda_permissions = (
            self._invoke_codebuild_lambda_permissions()
        )

        # CODEBUILD BUILD STATUS lambda
        self.codebuild_build_status_handler_zip = (
            self._codebuild_build_status_handler_zip()
        )
        self.codebuild_build_status_lambda_execution_role = (
            self._codebuild_build_status_lambda_execution_role()
        )
        self.codebuild_build_status_lambda = self._codebuild_build_status_lambda()
        self.codebuild_build_status_lambda_permissions = (
            self._codebuild_build_status_lambda_permissions()
        )

        # Slack BOT lambda build
        self.slack_bot_build_and_push_handler_zip = (
            self._slack_bot_build_and_push_handler_zip()
        )
        self.slack_bot_build_and_push_lambda_execution_role = (
            self._slack_bot_build_and_push_lambda_execution_role()
        )
        self.slack_bot_build_and_push_lambda = self._slack_bot_build_and_push_lambda()
        self.slack_bot_build_and_push_lambda_permissions = (
            self._slack_bot_build_and_push_lambda_permissions()
        )

        # Slack BOT lambda deploy
        self.slack_bot_deploy_handler_zip = self._slack_bot_deploy_handler_zip()
        self.slack_bot_deploy_lambda_execution_role = (
            self._slack_bot_deploy_lambda_execution_role()
        )
        self.slack_bot_deploy_lambda = self._slack_bot_deploy_lambda()
        self.slack_bot_deploy_lambda_permissions = (
            self._slack_bot_deploy_lambda_permissions()
        )

        # Slack BOT lambda build & deploy
        self.slack_bot_build_and_deploy_handler_zip = (
            self._slack_bot_build_and_deploy_handler_zip()
        )
        self.slack_bot_build_and_deploy_lambda_execution_role = (
            self._slack_bot_build_and_deploy_lambda_execution_role()
        )
        self.slack_bot_build_and_deploy_lambda = (
            self._slack_bot_build_and_deploy_lambda()
        )
        self.slack_bot_build_and_deploy_lambda_permissions = (
            self._slack_bot_build_and_deploy_lambda_permissions()
        )

        # AUTOMATION resource
        self.rest_api_resource_automation = self._rest_api_resource_automation()

        # INVOKE CODEBUILD resources
        self.rest_api_resource_invoke_codebuild = (
            self._rest_api_resource_invoke_codebuild()
        )
        self.rest_api_resource_codebuild_project_name = (
            self._rest_api_resource_codebuild_project_name()
        )
        self.invoke_codebuild_rest_api_method_put = (
            self._invoke_codebuild_rest_api_method_put()
        )
        self.invoke_codebuild_lambda_integration = (
            self._invoke_codebuild_lambda_integration()
        )

        # CODEBUILD BUILD STATUS resources
        self.rest_api_resource_codebuild_build_status = (
            self._rest_api_resource_codebuild_build_status()
        )
        self.rest_api_resource_codebuild_build_id = (
            self._rest_api_resource_codebuild_build_id()
        )
        self.codebuild_build_status_rest_api_method_get = (
            self._codebuild_build_status_rest_api_method_get()
        )
        self.codebuild_build_status_lambda_integration = (
            self._codebuild_build_status_lambda_integration()
        )

        # SLACK BOT root resources
        self.rest_api_resource_slack_bot = self._rest_api_resource_slack_bot()
        self.rest_api_resource_slack_bot_events = (
            self._rest_api_resource_slack_bot_events()
        )

        # SLACK BOT build_and_push resources
        self.rest_api_resource_slack_bot_events_build_and_push = (
            self._rest_api_resource_slack_bot_events_build_and_push()
        )
        self.slack_bot_events_build_and_push_rest_api_method_post = (
            self._slack_bot_events_build_and_push_rest_api_method_post()
        )
        self.slack_bot_events_build_and_push_lambda_integration = (
            self._slack_bot_events_build_and_push_lambda_integration()
        )

        # SLACK BOT deploy resources
        self.rest_api_resource_slack_bot_events_deploy = (
            self._rest_api_resource_slack_bot_events_deploy()
        )
        self.slack_bot_events_deploy_rest_api_method_post = (
            self._slack_bot_events_deploy_rest_api_method_post()
        )
        self.slack_bot_events_deploy_lambda_integration = (
            self._slack_bot_events_deploy_lambda_integration()
        )

        # SLACK BOT build_and_deploy resources
        self.rest_api_resource_slack_bot_events_build_and_deploy = (
            self._rest_api_resource_slack_bot_events_build_and_deploy()
        )
        self.slack_bot_events_build_and_deploy_rest_api_method_post = (
            self._slack_bot_events_build_and_deploy_rest_api_method_post()
        )
        self.slack_bot_events_build_and_deploy_lambda_integration = (
            self._slack_bot_events_build_and_deploy_lambda_integration()
        )

        self.rest_api_deployment = self._rest_api_deployment()
        self.rest_api_stage = self._rest_api_stage(
            rest_api_deployment=self.rest_api_deployment,
        )

        self.api_gateway_key = self._api_gateway_key()
        self.usage_plan = self._api_gateway_usage_plan()
        self.usage_plan_key = self._api_gateway_usage_plan_key()

        self.invoke_codebuild_curl_example_output = (
            self._put_invoke_codebuild_curl_example_output()
        )
        self.codebuild_build_status_curl_example_output = (
            self._get_codebuild_build_status_curl_example_output()
        )
        self.post_slack_bot_events_build_and_push_curl_example_output = (
            self._post_slack_bot_events_build_and_push_curl_example_output()
        )
        self.post_slack_bot_events_deploy_curl_example_output = (
            self._post_slack_bot_events_deploy_curl_example_output()
        )
        self.post_slack_bot_events_build_and_deploy_curl_example_output = (
            self._post_slack_bot_events_build_and_deploy_curl_example_output()
        )

    def _rest_api(self) -> ApiGatewayRestApi:
        name = self._name(object_type="api")

        return ApiGatewayRestApi(
            scope=self,
            id_=name,
            name=name,
            description="Automation Endpoints API Gateway.",
            disable_execute_api_endpoint=False,
            endpoint_configuration=ApiGatewayRestApiEndpointConfiguration(
                types=["EDGE"]
            ),
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            api_key_source="HEADER",
            provider=self.aws_provider,
            depends_on=[],
        )

    @staticmethod
    def _lambda_assume_role_policy() -> Dict[str, Any]:
        return {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": [
                            "lambda.amazonaws.com",
                        ]
                    },
                    "Action": "sts:AssumeRole",
                },
            ],
        }

    def _invoke_codebuild_handler_zip(self) -> DataArchiveFile:
        zip_file = self._zip_file_name(prefix="invoke-codebuild")

        return DataArchiveFile(
            scope=self,
            id=zip_file,
            type="zip",
            output_path=zip_file,
            source_dir=(
                f"{self.globals.cli_container_root}/"
                f"python3/"
                f"scripts/"
                f"automation_endpoints_stack/"
                f"invoke_codebuild"
            ),
            provider=self.archive_provider,
        )

    def _invoke_codebuild_lambda_execution_role(
        self,
    ) -> IamRole:
        name = "invoke-codebuild-lambda-execution-role"

        allow_start_codebuild = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "codebuild:StartBuild",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Action": ["sts:AssumeRole"],
                    # [ERROR] ClientError: An error occurred (AccessDenied) when calling the AssumeRole operation:
                    # User: arn:aws:sts::465525377090:assumed-role/codebuild-build-status-lambda-execution-role/automation-endpoints-codebuild-build-status-lambda-orchestra2
                    # is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::<>>:role/trust-orchestrating-account-iam-role-<>
                    "Resource": ["*"],  # TODO: shrink
                },
            ],
        }

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=json.dumps(self._lambda_assume_role_policy()),
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            ],
            inline_policy=[
                IamRoleInlinePolicy(
                    name="allow_invoke_codebuild",
                    policy=json.dumps(allow_start_codebuild),
                )
            ],
            provider=self.aws_provider,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
        )

    def _invoke_codebuild_lambda(self) -> LambdaFunction:
        name = self._name(object_type="invoke-codebuild-lambda")

        return LambdaFunction(
            scope=self,
            id_=name,
            function_name=name,
            runtime="python3.9",
            filename=self._zip_file_name(prefix="invoke-codebuild"),
            handler="handler.invoke_codebuild",
            role=self.invoke_codebuild_lambda_execution_role.arn,
            source_code_hash=self.invoke_codebuild_handler_zip.output_base64_sha256,
            environment=LambdaFunctionEnvironment(
                variables=self.sts_assume_roles | self.orchestra_account
            ),
            timeout=self.LAMBDA_TIMEOUT,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[
                self.invoke_codebuild_lambda_execution_role,
                self.invoke_codebuild_handler_zip,
            ],
        )

    def _invoke_codebuild_lambda_permissions(self) -> LambdaPermission:
        name = self._name(object_type="invoke-codebuild-lambda-permissions")

        return LambdaPermission(
            scope=self,
            id_=name,
            statement_id="AllowAPIGatewayInvocation",
            action="lambda:InvokeFunction",
            function_name=self.invoke_codebuild_lambda.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=f"{self.rest_api.execution_arn}/*",
            provider=self.aws_provider,
            depends_on=[self.rest_api, self.invoke_codebuild_lambda],
        )

    def _codebuild_build_status_handler_zip(self) -> DataArchiveFile:
        zip_file = self._zip_file_name(prefix="codebuild-build-status")

        return DataArchiveFile(
            scope=self,
            id=zip_file,
            type="zip",
            output_path=zip_file,
            source_dir=(
                f"{self.globals.cli_container_root}/"
                f"python3/"
                f"scripts/"
                f"automation_endpoints_stack/"
                f"codebuild_build_status"
            ),
            provider=self.archive_provider,
        )

    def _codebuild_build_status_lambda_execution_role(
        self,
    ) -> IamRole:
        name = "codebuild-build-status-lambda-execution-role"

        # TODO: Warning: inline_policy Argument is deprecated
        allow_get_codebuild_status = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "codebuild:BatchGetBuilds",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Action": ["sts:AssumeRole"],
                    # [ERROR] ClientError: An error occurred (AccessDenied) when calling the AssumeRole operation:
                    # User: arn:aws:sts::<head_account_aws_account_id>:assumed-role/codebuild-build-status-lambda-execution-role/automation-endpoints-codebuild-build-status-lambda-<heat_tenant>
                    # is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::<aws_account_id>:role/trust-orchestrating-account-iam-role-<tenant>
                    "Resource": ["*"],  # TODO: shrink
                },
            ],
        }

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=json.dumps(self._lambda_assume_role_policy()),
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            ],
            inline_policy=[
                IamRoleInlinePolicy(
                    name="allow_get_codebuild_status",
                    policy=json.dumps(allow_get_codebuild_status),
                )
            ],
            provider=self.aws_provider,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
        )

    def _codebuild_build_status_lambda(self) -> LambdaFunction:
        name = self._name(object_type="codebuild-build-status-lambda")

        return LambdaFunction(
            scope=self,
            id_=name,
            function_name=name,
            runtime="python3.9",
            filename=self._zip_file_name(prefix="codebuild-build-status"),
            handler="handler.codebuild_build_status",
            role=self.codebuild_build_status_lambda_execution_role.arn,
            source_code_hash=self.codebuild_build_status_handler_zip.output_base64_sha256,
            environment=LambdaFunctionEnvironment(
                variables=self.sts_assume_roles | self.orchestra_account
            ),
            timeout=self.LAMBDA_TIMEOUT,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[
                self.codebuild_build_status_lambda_execution_role,
                self.codebuild_build_status_handler_zip,
            ],
        )

    def _codebuild_build_status_lambda_permissions(self) -> LambdaPermission:
        name = self._name(object_type="codebuild-build-status-lambda-permissions")

        return LambdaPermission(
            scope=self,
            id_=name,
            statement_id="AllowAPIGatewayInvocation",
            action="lambda:InvokeFunction",
            function_name=self.codebuild_build_status_lambda.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=f"{self.rest_api.execution_arn}/*",
            provider=self.aws_provider,
            depends_on=[self.rest_api, self.codebuild_build_status_lambda],
        )

    def _slack_bot_build_and_push_handler_zip(self) -> DataArchiveFile:
        zip_file = self._zip_file_name(prefix="build-and-push")

        return DataArchiveFile(
            scope=self,
            id=zip_file,
            type="zip",
            output_path=zip_file,
            source_dir=(
                f"{self.globals.cli_container_root}/"
                "python3/"
                "scripts/"
                "automation_endpoints_stack/"
                "sb_build_and_push"
            ),
            provider=self.archive_provider,
        )

    def _slack_bot_build_and_push_lambda_execution_role(
        self,
    ) -> IamRole:
        name = "codebuild-slack-bot-build-execution-role"

        # TODO: Warning: inline_policy Argument is deprecated

        allow_get_codebuild_status = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "codebuild:BatchGetBuilds",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                {
                    "Action": "codebuild:StartBuild",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                # {
                #     "Sid": "Statement1",
                #     "Effect": "Allow",
                #     "Action": ["sts:AssumeRole"],
                #     # [ERROR] ClientError: An error occurred (AccessDenied) when calling the AssumeRole operation:
                #     # User: arn:aws:sts::<head_account_aws_account_id>:assumed-role/codebuild-build-status-lambda-execution-role/automation-endpoints-codebuild-build-status-lambda-<heat_tenant>
                #     # is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::<aws_account_id>:role/trust-orchestrating-account-iam-role-<tenant>
                #     "Resource": ["*"],  # TODO: shrink
                # },
            ],
        }

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=json.dumps(self._lambda_assume_role_policy()),
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            ],
            inline_policy=[
                IamRoleInlinePolicy(
                    name="allow_get_codebuild_status",
                    policy=json.dumps(allow_get_codebuild_status),
                )
            ],
            provider=self.aws_provider,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
        )

    def _slack_bot_build_and_push_lambda(self) -> LambdaFunction:
        name = self._name(object_type="build-and-push-lambda")

        return LambdaFunction(
            scope=self,
            id_=name,
            function_name=name,
            runtime="python3.9",
            filename=self._zip_file_name(prefix="build-and-push"),
            handler="handler.build_and_push",
            role=self.slack_bot_build_and_push_lambda_execution_role.arn,
            source_code_hash=self.slack_bot_build_and_push_handler_zip.output_base64_sha256,
            environment=LambdaFunctionEnvironment(
                variables=self.slack_signing_secret
                | self.slack_signing_secret_og
                | self.ci_job_token
                | self.orchestra_account
                | {"AWS_ACCOUNT_ID": self.globals.aws_account_id}
                | {
                    "ALLOWED_CHANNELS": json.dumps(
                        ArrangerConf.SLACK_COMMANDS["build_and_push"][
                            "allowed_channels"
                        ]
                    )
                }
            ),
            timeout=self.LAMBDA_TIMEOUT,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[
                self.slack_bot_build_and_push_lambda_execution_role,
                self.slack_bot_build_and_push_handler_zip,
            ],
        )

    def _slack_bot_build_and_push_lambda_permissions(self) -> LambdaPermission:
        name = self._name(object_type="slack-bot-build-and-push-lambda-permissions")

        return LambdaPermission(
            scope=self,
            id_=name,
            statement_id="AllowAPIGatewayInvocation",
            action="lambda:InvokeFunction",
            function_name=self.slack_bot_build_and_push_lambda.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=f"{self.rest_api.execution_arn}/*",
            provider=self.aws_provider,
            depends_on=[self.rest_api, self.slack_bot_build_and_push_lambda],
        )

    def _slack_bot_deploy_handler_zip(self) -> DataArchiveFile:
        zip_file = self._zip_file_name(prefix="deploy")

        return DataArchiveFile(
            scope=self,
            id=zip_file,
            type="zip",
            output_path=zip_file,
            source_dir=(
                f"{self.globals.cli_container_root}/"
                "python3/"
                "scripts/"
                "automation_endpoints_stack/"
                "sb_deploy"
            ),
            provider=self.archive_provider,
        )

    def _slack_bot_deploy_lambda_execution_role(
        self,
    ) -> IamRole:
        name = "codebuild-slack-bot-deploy-execution-role"

        # TODO: Warning: inline_policy Argument is deprecated

        allow_get_codebuild_status = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "codebuild:BatchGetBuilds",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                {
                    "Action": "codebuild:StartBuild",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                # {
                #     "Sid": "Statement1",
                #     "Effect": "Allow",
                #     "Action": ["sts:AssumeRole"],
                #     # [ERROR] ClientError: An error occurred (AccessDenied) when calling the AssumeRole operation:
                #     # User: arn:aws:sts::<head_account_aws_account_id>:assumed-role/codebuild-build-status-lambda-execution-role/automation-endpoints-codebuild-build-status-lambda-<heat_tenant>
                #     # is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::<aws_account_id>:role/trust-orchestrating-account-iam-role-<tenant>
                #     "Resource": ["*"],  # TODO: shrink
                # },
            ],
        }

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=json.dumps(self._lambda_assume_role_policy()),
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            ],
            inline_policy=[
                IamRoleInlinePolicy(
                    name="allow_get_codebuild_status",
                    policy=json.dumps(allow_get_codebuild_status),
                )
            ],
            provider=self.aws_provider,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
        )

    def _slack_bot_deploy_lambda(self) -> LambdaFunction:
        name = self._name(object_type="deploy-lambda")

        return LambdaFunction(
            scope=self,
            id_=name,
            function_name=name,
            runtime="python3.9",
            filename=self._zip_file_name(prefix="deploy"),
            handler="handler.deploy",
            role=self.slack_bot_deploy_lambda_execution_role.arn,
            source_code_hash=self.slack_bot_deploy_handler_zip.output_base64_sha256,
            environment=LambdaFunctionEnvironment(
                variables=self.slack_signing_secret
                | self.slack_signing_secret_og
                | self.orchestra_account
                | {"AWS_ACCOUNT_ID": self.globals.aws_account_id}
                | {
                    "ALLOWED_CHANNELS": json.dumps(
                        ArrangerConf.SLACK_COMMANDS["deploy"]["allowed_channels"]
                    )
                }
            ),
            timeout=self.LAMBDA_TIMEOUT,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[
                self.slack_bot_deploy_lambda_execution_role,
                self.slack_bot_deploy_handler_zip,
            ],
        )

    def _slack_bot_deploy_lambda_permissions(self) -> LambdaPermission:
        name = self._name(object_type="slack-bot-deploy-lambda-permissions")

        return LambdaPermission(
            scope=self,
            id_=name,
            statement_id="AllowAPIGatewayInvocation",
            action="lambda:InvokeFunction",
            function_name=self.slack_bot_deploy_lambda.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=f"{self.rest_api.execution_arn}/*",
            provider=self.aws_provider,
            depends_on=[self.rest_api, self.slack_bot_deploy_lambda],
        )

    def _slack_bot_build_and_deploy_handler_zip(self) -> DataArchiveFile:
        zip_file = self._zip_file_name(prefix="build_and_deploy")

        return DataArchiveFile(
            scope=self,
            id=zip_file,
            type="zip",
            output_path=zip_file,
            source_dir=(
                f"{self.globals.cli_container_root}/"
                "python3/"
                "scripts/"
                "automation_endpoints_stack/"
                "sb_build_and_deploy"
            ),
            provider=self.archive_provider,
        )

    def _slack_bot_build_and_deploy_lambda_execution_role(
        self,
    ) -> IamRole:
        name = "codebuild-slack-bot-build_and_deploy-execution-role"

        # TODO: Warning: inline_policy Argument is deprecated

        allow_get_codebuild_status = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "codebuild:BatchGetBuilds",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                {
                    "Action": "codebuild:StartBuild",
                    "Resource": "*",
                    "Effect": "Allow",
                },
                # {
                #     "Sid": "Statement1",
                #     "Effect": "Allow",
                #     "Action": ["sts:AssumeRole"],
                #     # [ERROR] ClientError: An error occurred (AccessDenied) when calling the AssumeRole operation:
                #     # User: arn:aws:sts::<head_account_aws_account_id>:assumed-role/codebuild-build-status-lambda-execution-role/automation-endpoints-codebuild-build-status-lambda-<heat_tenant>
                #     # is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::<aws_account_id>:role/trust-orchestrating-account-iam-role-<tenant>
                #     "Resource": ["*"],  # TODO: shrink
                # },
            ],
        }

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=json.dumps(self._lambda_assume_role_policy()),
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            ],
            inline_policy=[
                IamRoleInlinePolicy(
                    name="allow_get_codebuild_status",
                    policy=json.dumps(allow_get_codebuild_status),
                )
            ],
            provider=self.aws_provider,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
        )

    def _slack_bot_build_and_deploy_lambda(self) -> LambdaFunction:
        name = self._name(object_type="build-and-deploy-lambda")

        return LambdaFunction(
            scope=self,
            id_=name,
            function_name=name,
            runtime="python3.9",
            filename=self._zip_file_name(prefix="build_and_deploy"),
            handler="handler.build_and_deploy",
            role=self.slack_bot_build_and_deploy_lambda_execution_role.arn,
            source_code_hash=self.slack_bot_build_and_deploy_handler_zip.output_base64_sha256,
            environment=LambdaFunctionEnvironment(
                variables=self.slack_signing_secret
                | self.slack_signing_secret_og
                | self.orchestra_account
                | {"AWS_ACCOUNT_ID": self.globals.aws_account_id}
                | {
                    "ALLOWED_CHANNELS": json.dumps(
                        ArrangerConf.SLACK_COMMANDS["build_and_deploy"][
                            "allowed_channels"
                        ]
                    )
                }
            ),
            timeout=self.LAMBDA_TIMEOUT,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[
                self.slack_bot_build_and_deploy_lambda_execution_role,
                self.slack_bot_build_and_deploy_handler_zip,
            ],
        )

    def _slack_bot_build_and_deploy_lambda_permissions(self) -> LambdaPermission:
        name = self._name(object_type="slack-bot-build-and-deploy-lambda-permissions")

        return LambdaPermission(
            scope=self,
            id_=name,
            statement_id="AllowAPIGatewayInvocation",
            action="lambda:InvokeFunction",
            function_name=self.slack_bot_build_and_deploy_lambda.function_name,
            principal="apigateway.amazonaws.com",
            source_arn=f"{self.rest_api.execution_arn}/*",
            provider=self.aws_provider,
            depends_on=[self.rest_api, self.slack_bot_build_and_deploy_lambda],
        )

    def _rest_api_resource_automation(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-automation")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api.root_resource_id,
            path_part="automation",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api],
        )

    def _rest_api_resource_invoke_codebuild(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-invoke-codebuild")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_automation.id,
            path_part="invoke_codebuild",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_automation],
        )

    def _rest_api_resource_codebuild_project_name(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-codebuild-project-name")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_invoke_codebuild.id,
            path_part="{codebuild_project_name}",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_invoke_codebuild],
        )

    def _invoke_codebuild_rest_api_method_put(self) -> ApiGatewayMethod:
        name = self._name("invoke-codebuild-method-put")

        return ApiGatewayMethod(
            scope=self,
            id_=name,
            authorization="NONE",
            http_method="PUT",
            resource_id=self.rest_api_resource_codebuild_project_name.id,
            rest_api_id=self.rest_api.id,
            api_key_required=True,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_codebuild_project_name],
        )

    def _invoke_codebuild_lambda_integration(self) -> ApiGatewayIntegration:
        name = self._name(object_type="invoke-codebuild-lambda-integration")

        return ApiGatewayIntegration(
            scope=self,
            id_=name,
            http_method="PUT",
            resource_id=self.rest_api_resource_codebuild_project_name.id,
            rest_api_id=self.rest_api.id,
            type="AWS_PROXY",
            uri=self.invoke_codebuild_lambda.invoke_arn,
            # POST-method is used intentionally:
            #   https://stackoverflow.com/questions/63625888/terraform-api-gateway-lambda-integration-trigger-problem
            integration_http_method="POST",
            depends_on=[
                self.rest_api_resource_codebuild_project_name,
                self.invoke_codebuild_lambda,
            ],
        )

    def _rest_api_resource_codebuild_build_status(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-codebuild-build-status")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_automation.id,
            path_part="codebuild_build_status",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_automation],
        )

    def _rest_api_resource_codebuild_build_id(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-codebuild-build-id")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_codebuild_build_status.id,
            path_part="{codebuild_build_id}",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_codebuild_build_status],
        )

    def _codebuild_build_status_rest_api_method_get(self) -> ApiGatewayMethod:
        name = self._name("codebuild-build-status-method-get")

        return ApiGatewayMethod(
            scope=self,
            id_=name,
            authorization="NONE",
            http_method="GET",
            resource_id=self.rest_api_resource_codebuild_build_id.id,
            rest_api_id=self.rest_api.id,
            api_key_required=True,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_codebuild_build_id],
        )

    def _codebuild_build_status_lambda_integration(self) -> ApiGatewayIntegration:
        name = self._name(object_type="codebuild-build-status-lambda-integration")

        return ApiGatewayIntegration(
            scope=self,
            id_=name,
            http_method="GET",
            resource_id=self.rest_api_resource_codebuild_build_id.id,
            rest_api_id=self.rest_api.id,
            type="AWS_PROXY",
            uri=self.codebuild_build_status_lambda.invoke_arn,
            # POST-method is used intentionally:
            #   https://stackoverflow.com/questions/63625888/terraform-api-gateway-lambda-integration-trigger-problem
            integration_http_method="POST",
            depends_on=[
                self.rest_api_resource_codebuild_build_id,
                self.codebuild_build_status_lambda,
            ],
        )

    def _rest_api_resource_slack_bot(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-slack-bot-build-and-push")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_automation.id,
            path_part="slack",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_automation],
        )

    def _rest_api_resource_slack_bot_events(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-codebuild-slack-bot-events")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_slack_bot.id,
            path_part="events",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot],
        )

    def _rest_api_resource_slack_bot_events_build_and_push(self) -> ApiGatewayResource:
        name = self._name(
            object_type="rest-api-resource-slack-bot-events-build-and-push"
        )

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_slack_bot_events.id,
            path_part="build_and_push",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot_events],
        )

    def _slack_bot_events_build_and_push_rest_api_method_post(self) -> ApiGatewayMethod:
        name = self._name("slack-bot-events-build-and-push-method-post")

        return ApiGatewayMethod(
            scope=self,
            id_=name,
            authorization="NONE",
            http_method="POST",
            resource_id=self.rest_api_resource_slack_bot_events_build_and_push.id,
            rest_api_id=self.rest_api.id,
            api_key_required=False,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot_events_build_and_push],
        )

    def _slack_bot_events_build_and_push_lambda_integration(
        self,
    ) -> ApiGatewayIntegration:
        name = self._name(object_type="build-and-push-lambda-integration")

        return ApiGatewayIntegration(
            scope=self,
            id_=name,
            http_method="POST",
            resource_id=self.rest_api_resource_slack_bot_events_build_and_push.id,
            rest_api_id=self.rest_api.id,
            type="AWS_PROXY",
            uri=self.slack_bot_build_and_push_lambda.invoke_arn,
            # POST-method is used intentionally:
            #   https://stackoverflow.com/questions/63625888/terraform-api-gateway-lambda-integration-trigger-problem
            integration_http_method="POST",
            depends_on=[
                self.rest_api_resource_slack_bot_events_build_and_push,
                self.slack_bot_build_and_push_lambda,
            ],
        )

    def _rest_api_resource_slack_bot_events_deploy(self) -> ApiGatewayResource:
        name = self._name(object_type="rest-api-resource-slack-bot-events-deploy")

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_slack_bot_events.id,
            path_part="deploy",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot_events],
        )

    def _slack_bot_events_deploy_rest_api_method_post(self) -> ApiGatewayMethod:
        name = self._name("slack-bot-events-deploy-method-post")

        return ApiGatewayMethod(
            scope=self,
            id_=name,
            authorization="NONE",
            http_method="POST",
            resource_id=self.rest_api_resource_slack_bot_events_deploy.id,
            rest_api_id=self.rest_api.id,
            api_key_required=False,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot_events_deploy],
        )

    def _slack_bot_events_deploy_lambda_integration(
        self,
    ) -> ApiGatewayIntegration:
        name = self._name(object_type="deploy-lambda-integration")

        return ApiGatewayIntegration(
            scope=self,
            id_=name,
            http_method="POST",
            resource_id=self.rest_api_resource_slack_bot_events_deploy.id,
            rest_api_id=self.rest_api.id,
            type="AWS_PROXY",
            uri=self.slack_bot_deploy_lambda.invoke_arn,
            # POST-method is used intentionally:
            #   https://stackoverflow.com/questions/63625888/terraform-api-gateway-lambda-integration-trigger-problem
            integration_http_method="POST",
            depends_on=[
                self.rest_api_resource_slack_bot_events_build_and_push,
                self.slack_bot_build_and_push_lambda,
            ],
        )

    def _rest_api_resource_slack_bot_events_build_and_deploy(
        self,
    ) -> ApiGatewayResource:
        name = self._name(
            object_type="rest-api-resource-slack-bot-events-build_and_deploy"
        )

        return ApiGatewayResource(
            scope=self,
            id_=name,
            parent_id=self.rest_api_resource_slack_bot_events.id,
            path_part="build_and_deploy",
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot_events],
        )

    def _slack_bot_events_build_and_deploy_rest_api_method_post(
        self,
    ) -> ApiGatewayMethod:
        name = self._name("slack-bot-events-build-and-deploy-method-post")

        return ApiGatewayMethod(
            scope=self,
            id_=name,
            authorization="NONE",
            http_method="POST",
            resource_id=self.rest_api_resource_slack_bot_events_build_and_deploy.id,
            rest_api_id=self.rest_api.id,
            api_key_required=False,
            provider=self.aws_provider,
            depends_on=[self.rest_api_resource_slack_bot_events_build_and_deploy],
        )

    def _slack_bot_events_build_and_deploy_lambda_integration(
        self,
    ) -> ApiGatewayIntegration:
        name = self._name(object_type="build-and-deploy-lambda-integration")

        return ApiGatewayIntegration(
            scope=self,
            id_=name,
            http_method="POST",
            resource_id=self.rest_api_resource_slack_bot_events_build_and_deploy.id,
            rest_api_id=self.rest_api.id,
            type="AWS_PROXY",
            uri=self.slack_bot_build_and_deploy_lambda.invoke_arn,
            # POST-method is used intentionally:
            #   https://stackoverflow.com/questions/63625888/terraform-api-gateway-lambda-integration-trigger-problem
            integration_http_method="POST",
            depends_on=[
                self.rest_api_resource_slack_bot_events_build_and_push,
                self.slack_bot_build_and_push_lambda,
            ],
        )

    def _rest_api_deployment(self) -> ApiGatewayDeployment:
        name = self._name(object_type="rest-api-deployment")

        lambda_integrations = [
            self.invoke_codebuild_lambda_integration,
            self.codebuild_build_status_lambda_integration,
            self.slack_bot_events_build_and_push_lambda_integration,
            self.slack_bot_events_deploy_lambda_integration,
            self.slack_bot_events_build_and_deploy_lambda_integration,
        ]

        return ApiGatewayDeployment(
            scope=self,
            id_=name,
            rest_api_id=self.rest_api.id,
            provider=self.aws_provider,
            lifecycle=TerraformResourceLifecycle(
                create_before_destroy=True,
            ),
            triggers={"number_of_lambdas_changes": str(len(lambda_integrations))},
            depends_on=lambda_integrations,
        )

    def _rest_api_stage(
        self, rest_api_deployment: ApiGatewayDeployment
    ) -> ApiGatewayStage:
        name = self._name(object_type="rest-api-stage-v1")

        return ApiGatewayStage(
            scope=self,
            id_=name,
            deployment_id=rest_api_deployment.id,
            rest_api_id=self.rest_api.id,
            stage_name=self.STAGE_NAME,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[rest_api_deployment],
        )

    def _api_gateway_key(self) -> ApiGatewayApiKey:
        name = self._name(object_type="api-gateway-key")

        return ApiGatewayApiKey(
            scope=self,
            id_=name,
            name=name,
            description="X-API-KEY for accessing automation endpoints API Gateway.",
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            value=self.globals.aws_sm_secret(
                secret_name=f"{self.globals.tenant}/automation_endpoints"
            )["API_GATEWAY_API_KEY"],
            provider=self.aws_provider,
        )

    def _api_gateway_usage_plan(self) -> ApiGatewayUsagePlan:
        name = self._name(object_type="usage-plan")

        return ApiGatewayUsagePlan(
            scope=self,
            id_=name,
            name=name,
            api_stages=[
                ApiGatewayUsagePlanApiStages(
                    api_id=self.rest_api.id, stage=self.rest_api_stage.stage_name
                )
            ],
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[self.rest_api_stage],
        )

    def _api_gateway_usage_plan_key(self) -> ApiGatewayUsagePlanKey:
        name = self._name(object_type="usage-plan-key")

        return ApiGatewayUsagePlanKey(
            scope=self,
            id_=name,
            key_id=self.api_gateway_key.id,
            key_type="API_KEY",
            usage_plan_id=self.usage_plan.id,
            depends_on=[self.api_gateway_key, self.usage_plan],
        )

    def _put_invoke_codebuild_curl_example_output(self) -> TerraformOutput:
        return TerraformOutput(
            scope=self,
            id="invoke_codebuild_curl_example",
            description="CURL example to invoke invoke_codebuild lambda.",
            value=(
                f"curl -X PUT -v -H 'x-api-key: <API_KEY>' "
                '--data \'{"GIT_REF": "main"}\' '
                f"{self.rest_api_stage.invoke_url}/"
                f"{self.rest_api_resource_automation.path_part}/"
                f"{self.rest_api_resource_invoke_codebuild.path_part}/"
                f"<codebuild_project_name>"
            ),
        )

    def _get_codebuild_build_status_curl_example_output(self) -> TerraformOutput:
        return TerraformOutput(
            scope=self,
            id="codebuild_build_status_curl_example",
            description="CURL example to invoke codebuild_build_status lambda.",
            value=(
                f"curl -X GET -v -H 'x-api-key: <API_KEY>' "
                f"{self.rest_api_stage.invoke_url}/"
                f"{self.rest_api_resource_automation.path_part}/"
                f"{self.rest_api_resource_codebuild_build_status.path_part}/"
                "<codebuild_build_name:codebuild_build_id>"
            ),
        )

    def _post_slack_bot_events_build_and_push_curl_example_output(
        self,
    ) -> TerraformOutput:
        return TerraformOutput(
            scope=self,
            id="slack_bot_events_build_and_push_curl_example",
            description="CURL example to invoke slack_bot_build_and_push lambda.",
            value=(
                f"curl -X POST -v -H 'x-api-key: <API_KEY>' "
                "--data '{}' "
                f"{self.rest_api_stage.invoke_url}/"
                f"{self.rest_api_resource_automation.path_part}/"
                "slack/events/"
                f"{self.rest_api_resource_slack_bot_events_build_and_push.path_part}"
            ),
        )

    def _post_slack_bot_events_deploy_curl_example_output(
        self,
    ) -> TerraformOutput:
        return TerraformOutput(
            scope=self,
            id="slack_bot_events_deploy_curl_example",
            description="CURL example to invoke slack_bot_deploy lambda.",
            value=(
                f"curl -X POST -v -H 'x-api-key: <API_KEY>' "
                "--data '{}' "
                f"{self.rest_api_stage.invoke_url}/"
                f"{self.rest_api_resource_automation.path_part}/"
                "slack/events/"
                f"{self.rest_api_resource_slack_bot_events_deploy.path_part}"
            ),
        )

    def _post_slack_bot_events_build_and_deploy_curl_example_output(
        self,
    ) -> TerraformOutput:
        return TerraformOutput(
            scope=self,
            id="slack_bot_events_build_and_deploy_curl_example",
            description="CURL example to invoke slack_bot_build_and_deploy lambda.",
            value=(
                f"curl -X POST -v -H 'x-api-key: <API_KEY>' "
                "--data '{}' "
                f"{self.rest_api_stage.invoke_url}/"
                f"{self.rest_api_resource_automation.path_part}/"
                "slack/events/"
                f"{self.rest_api_resource_slack_bot_events_build_and_deploy.path_part}"
            ),
        )

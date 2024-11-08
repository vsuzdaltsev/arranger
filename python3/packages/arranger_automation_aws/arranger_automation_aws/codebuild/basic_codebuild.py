from functools import reduce
import random
import time

from typing import Dict, List, Tuple, Union

from arranger_automation.log import Log
from arranger_automation_aws.client import AwsClient


def _env_var(name: str, value: str) -> Dict[str, str]:
    return {"name": name, "value": value, "type": "PLAINTEXT"}


class BasicCodebuild:
    SLEEP_BETWEEN_TRIES = 60

    def __init__(
        self,
        project_name: str,
        boto_client: type(AwsClient),
        source_version_override: Union[str, None] = None,
        environment_variables_overrides: Union[List[Dict[str, str]], None] = None,
    ):
        self.log = Log().logger(desc=self.__class__.__name__)
        self.project_name = project_name
        self.boto_client = boto_client
        self.source_version_override = source_version_override
        self.environment_variables_overrides = environment_variables_overrides

        if not self.environment_variables_overrides:
            self.environment_variables_overrides = []

        self.build_id = None

    @classmethod
    def projects(cls, boto_client: type(AwsClient)) -> List[str]:
        projects = []

        for page in boto_client.get_paginator("list_projects").paginate():
            projects.extend(page.get("projects"))

        return sorted(projects)

    @classmethod
    def builds_for_project(
        cls, boto_client: type(AwsClient), project_name: str
    ) -> List[str]:
        builds = []

        for page in boto_client.get_paginator("list_builds_for_project").paginate(
            projectName=project_name
        ):
            builds.extend(page.get("ids"))

        return sorted(builds)

    def invoke(self) -> Tuple:
        response = self.boto_client.start_build(**self._invocation_params())
        time.sleep(self._sleep_between_iterations())
        self.log.debug(f">> Start build response: {response}.")

        return self._wait_for(response=response)

    def _invocation_params(self) -> Dict:
        params = {
            "projectName": self.project_name,
            "environmentVariablesOverride": self._format_env_overrides(),
        }
        if self.source_version_override:
            params.update({"sourceVersion": self.source_version_override})

        return params

    def _format_env_overrides(self) -> List[Dict[str, str]]:
        envs = []
        for item in self.environment_variables_overrides:
            name, value = next(iter(item.items()))
            envs.append(_env_var(name=name, value=value))

        return envs

    def _wait_for(self, response: Dict) -> Tuple[str, str]:
        self.build_id = response.get("build", {}).get("id")

        state = self._get_build_status()

        while state == "IN_PROGRESS":
            sleep_for_iteration = self._sleep_between_iterations()
            build_info = self._build_info(response, state)

            self.log.info(f">> {build_info} Sleep for {sleep_for_iteration} seconds.")

            time.sleep(sleep_for_iteration)
            state = self._get_build_status()
            build_info = self._build_info(response, state)

            self.log.debug(f">> Build info: {build_info}.")

        return self.build_id, state

    def _sleep_between_iterations(self) -> int:
        return random.randrange(0, self.SLEEP_BETWEEN_TRIES)

    def _build_info(self, response: Dict, state: str) -> str:
        response_env_vars = [
            {var["name"]: var["value"]}
            for var in response["build"]["environment"]["environmentVariables"]
        ]
        env_vars = reduce(lambda a, b: dict(a, **b), response_env_vars)

        return " ".join(
            [
                f"Build {self.build_id}.",
                f"Environment variables: {env_vars}.",
                f"State: {state}.",
            ]
        )

    def _get_build_status(self) -> str:
        response = self.boto_client.batch_get_builds(ids=[self.build_id])
        status = response["builds"][0]["buildStatus"]

        return status


if __name__ == "__main__":
    client = AwsClient(
        name="codebuild", region="eu-west-2", aws_profile="develop1"
    ).client

    print(f">> Codebuild_projects: {BasicCodebuild.projects(boto_client=client)}.")
    print(
        BasicCodebuild(
            project_name="universal_build_back_develop1",
            boto_client=client,
            environment_variables_overrides=[
                {
                    "SERVICE_GIT_REF": "main",
                    "LOG_LEVEL": "info",
                    "META_SERVICE_CODEBUILD_IMAGE_TAG": "latest",
                    "SERVICES": "crypto-service-ms",
                    "ADDITIONAL_TAGS": "",
                }
            ],
        ).invoke()
    )

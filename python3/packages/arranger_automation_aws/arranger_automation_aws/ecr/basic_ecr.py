"""Create/remove AWS Elastic Container Registry repos."""

import json
import os
from typing import List, NoReturn, Union

from boto3 import client as ecr
from boto3 import session as ecr_session

from arranger_automation.log import Log


class BasicEcr:
    """Manage AWS ECR creation/deletion."""

    KEEP_IMAGES_COUNT = 3
    """Keep not more that N images."""
    DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION") or "us-east-1"
    """Default region for creating ECR repos."""

    def __init__(
        self,
        repository_name: str,
        region_name: str = None,
        keep_images_count: int = KEEP_IMAGES_COUNT,
        credentials=None,
        aws_profile=None,
    ):
        self.log = Log.logger(desc=type(self).__name__)
        self.repository_name = repository_name
        self.keep_images_count = keep_images_count
        self.region_name = self._setup_region_name(region_name)
        self.aws_profile = aws_profile

        if credentials:
            self.client = ecr("ecr", region_name=self.region_name, **credentials)

        if not credentials and aws_profile:
            self.client = ecr_session.Session(profile_name=self.aws_profile).client(
                "ecr", region_name=self.region_name
            )
        else:
            raise RuntimeError("Failed to authorize ECR client.")

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def _registry_id(self) -> str:
        """The same that current AWS Account ID."""
        return self.client.describe_registry()["registryId"]

    def _available_repositories(self) -> List:
        """List of available AWS ECR repositories within the registry of the given account/region."""
        paginator = self.client.get_paginator("describe_repositories").paginate()
        all_repos = []
        for repos in paginator:
            all_repos += repos["repositories"]

        return [repo["repositoryName"] for repo in all_repos]

    def _repository_exist(self) -> bool:
        """Does the AWS ECR repository exist within the registry of the given account/region?"""
        return self.repository_name in self._available_repositories()

    def _create_repository(self) -> bool:
        """Call AWS ECR repository creation with given name/region."""
        try:
            self.client.create_repository(repositoryName=self.repository_name)

            return True
        except self.client.exceptions.RepositoryAlreadyExistsException as err:
            self.log.error(">> Can't create %s. Error: %s", self.repository_name, err)

            return False

    def _policy(self) -> str:
        """AWS ECR Life cycle policy for the created repository."""
        return json.dumps(
            {
                "rules": [
                    {
                        "rulePriority": 1,
                        "description": f"Only keep {self.keep_images_count} untagged images",
                        "selection": {
                            "tagStatus": "untagged",
                            "countType": "imageCountMoreThan",
                            "countNumber": self.keep_images_count,
                        },
                        "action": {"type": "expire"},
                    }
                ]
            }
        )

    def _put_life_cycle_policy(self) -> Union[bool, NoReturn]:
        """Attach AWS ECR life cycle policy to the repository."""
        try:
            self.client.put_lifecycle_policy(
                registryId=self._registry_id(),
                repositoryName=self.repository_name,
                lifecyclePolicyText=self._policy(),
            )
            return True
        except BaseException as err:
            self.log.error(
                ">> Couldn't put life cycle policy for %s AWS ECR repo. Error: %s",
                self.repository_name,
                err,
            )
            raise RuntimeError(
                f">> Error putting life cycle policy to {self.repository_name}."
            ) from err

    def _setup_region_name(self, region_name: Union[str, None] = None) -> str:
        """Setup AWS ECR client region name."""
        if not region_name:
            self.log.debug(
                ">> %s: no AWS region given, using default: %s",
                __class__.__name__,
                self.DEFAULT_REGION,
            )
            return self.DEFAULT_REGION

        return region_name

    def prepare_repository(self) -> Union[bool, NoReturn]:
        """Create AWS ECR repository and then attach given life cycle policy to it."""
        try:
            if self._repository_exist():
                self.log.warning(
                    ">> The %s repository already exists.", self.repository_name
                )
                self._put_life_cycle_policy()

                return False

            self._create_repository()
            self._put_life_cycle_policy()

            return True
        except BaseException as err:
            self.log.error(">> Couldn't prepare AWS ECR repo. Error: %s", err)
            raise RuntimeError(
                f">> Error preparing {self.repository_name} AWS ECR repo."
            ) from err

    def delete_repository(self, force: bool = True) -> bool:
        """Delete given repository. Deletion is forced by default."""
        try:
            self.client.delete_repository(
                registryId=self._registry_id(),
                repositoryName=self.repository_name,
                force=force,
            )

            return True
        except self.client.exceptions.RepositoryNotFoundException as err:
            self.log.error(">> Can't delete %s. Error: %s", self.repository_name, err)

            return False

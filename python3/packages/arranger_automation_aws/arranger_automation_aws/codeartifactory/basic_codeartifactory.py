import subprocess

from arranger_automation_aws.client import AwsClient
from arranger_automation.log import Log


class MvnCodeartifactory:
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    @property
    def _repository(self):
        return "mvn"

    @property
    def _repository_format(self):
        return "maven"

    def __init__(self, aws_profile=None, credentials=None, region=None, domain=None):
        self.log = Log().logger(desc=self.__class__.__name__)
        self.aws_profile = aws_profile
        self.credentials = credentials
        self.region = region
        self.domain = domain

        self.client = AwsClient(
            "codeartifact",
            region=self.region,
            aws_profile=aws_profile,
            credentials=credentials,
        ).client

    def _list_package_version_assets(
        self,
        package=None,
        namespace=None,
        package_version=None,
    ):
        paginator = self.client.get_paginator("list_package_version_assets")

        return [
            asset.get("assets")
            for asset in paginator.paginate(
                domain=self.domain,
                repository=self._repository,
                package=package,
                format=self._repository_format,
                packageVersion=package_version,
                namespace=namespace,
            )
        ]

    def jars(self, namespace=None, package=None, package_version=None):
        all_assets = self._list_package_version_assets(
            package=package, namespace=namespace, package_version=package_version
        )
        jars = []
        for i, x in enumerate(all_assets):
            for j, y in enumerate(x):
                if ".jar" in y["name"]:
                    jars.append(y["name"])

        self.log.warning(f">> Existing jar files: {jars}.")

        return jars

    def download_jar(
        self, namespace=None, package=None, package_version=None, output_file=None
    ):
        latest_jar = self.jars(
            namespace=namespace, package=package, package_version=package_version
        )[0]

        if not output_file:
            output_file = latest_jar

        cmd = (
            f"aws codeartifact get-package-version-asset "
            f"--region {self.region} "
            f"--domain {self.domain} "
            f"--repository {self._repository} "
            f"--format {self._repository_format} "
            f"--namespace {namespace} "
            f"--package {package} "
            f"--package-version {package_version} "
            f"--asset {latest_jar} {output_file} "
        )

        if self.aws_profile:
            cmd += f"--profile {self.domain}"

        self.log.warning(f">> Download: {latest_jar} into {output_file}.")

        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) as proc:
            output = proc.stdout.read()
        self.log.debug(f">> Output: {output}.")

        return latest_jar


if __name__ == "__main__":
    mvn = MvnCodeartifactory(
        aws_profile="switchdev1", region="eu-west-2", domain="switchdev1"
    )
    print(f">> EXISTING JARS: {mvn.jars()}")
    mvn.download_jar(
        namespace="com.velox.switchpay",
        package="bank-gate-ms",
        package_version="0.0.1-SNAPSHOT",
        output_file=None,
    )

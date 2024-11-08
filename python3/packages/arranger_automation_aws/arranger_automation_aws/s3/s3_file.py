from typing import List, Union

from arranger_automation_aws.client import AwsClient
from arranger_automation.log import Log


class S3File:
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(
        self, bucket_name: str, aws_profile=None, credentials=None, region=None
    ):
        self.log = Log().logger(desc=self.__class__.__name__)
        self.aws_profile = aws_profile
        self.credentials = credentials
        self.region = region

        self.bucket_name = bucket_name
        self.client = AwsClient(
            "s3",
            region=self.region,
            aws_profile=aws_profile,
            credentials=credentials,
        ).client

    def _latest_version(self, input_file) -> str:
        response = self.client.list_object_versions(
            Bucket=self.bucket_name, Prefix=input_file
        )

        return response["Versions"][0]["VersionId"]

    def list_objects(self, page_size: int = 100) -> List[str]:
        objects = []
        paginator = self.client.get_paginator("list_objects_v2")
        operation_parameters = {
            "Bucket": self.bucket_name,
            "PaginationConfig": {"PageSize": page_size},
        }

        for page in paginator.paginate(**operation_parameters):
            if "Contents" in page:
                for obj in page["Contents"]:
                    objects.append(obj["Key"])

        return objects

    def copy_file_from_s3(
        self, input_file: str, output_file: str, version: Union[str, None] = None
    ) -> None:
        try:
            if not version:
                version = self._latest_version(input_file=input_file)

            self.log.debug(f">> File: {input_file}; version: {version}.")

            self.client.download_file(
                self.bucket_name,
                input_file,
                output_file,
                ExtraArgs={"VersionId": version},
            )
        except BaseException as some_error:
            raise RuntimeError(
                f"Couldn't copy {input_file} to {output_file}. Error: {some_error}."
            )

    def copy_local_file_to_s3(self, input_file: str, output_file: str) -> None:
        try:
            self.client.upload_file(input_file, self.bucket_name, output_file)
        except BaseException as some_error:
            raise RuntimeError(
                f"Couldn't copy {input_file} to s3://{self.bucket_name}/{output_file}. Error: {some_error}."
            )


if __name__ == "__main__":

    backup_bucket = "backup-ldap-staging1"
    s3 = S3File(aws_profile="sandbox1", region="eu-west-2", bucket_name=backup_bucket)
    s3.list_objects()
    # s3.copy_file_from_s3(
    #     input_file="Pipfile",
    #     output_file="Pipfile.bak",
    #     version="LSwb0b.LeQij78lHmRFXlhX9RmRSdaSE",
    # )
    # s3.copy_local_file_to_s3(input_file="neoswitch.net.backup.ldif", output_file="neoswitch.net.backup.ldif.new")
    s3.copy_file_from_s3(
        input_file="mydomain.net.backup.ldif",
        output_file="mydomain.net.backup.ldif.new",
    )

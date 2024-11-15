from typing import Dict, Union

from boto3 import session as ses
from botocore.exceptions import ClientError

from arranger_automation.log import Log


def camel_to_kebab(s):
    import re

    kebab = re.sub(r"(?<!^)(?=[A-Z])", "-", s).lower()
    return kebab


class BackendHelperAws:
    from arranger_conf.arranger_conf import ArrangerConf

    BUCKET_NAME = f"{ArrangerConf.PROJECT_NAME}-terraform-remote-states"[:63]

    @classmethod
    def s3client(cls, profile: str, aws_region="us-east-1") -> ses.Session:
        return ses.Session(profile_name=profile, region_name=aws_region).client("s3")

    @classmethod
    def enable_s3_versioning(cls, profile: str, aws_region="us-east-1"):
        ses.Session(profile_name=profile, region_name=aws_region).resource(
            "s3"
        ).BucketVersioning(cls.BUCKET_NAME).enable()

    @classmethod
    def dynamodb_client(cls, profile: str, aws_region: str) -> ses.Session.client:
        return ses.Session(profile_name=profile, region_name=aws_region).client(
            "dynamodb"
        )

    @classmethod
    def create_bucket(cls, profile: str, location_constraint: str) -> str:

        try:
            client = cls.s3client(profile=profile, aws_region=location_constraint)

            if location_constraint != "us-east-1":
                location = {
                    "CreateBucketConfiguration": {
                        "LocationConstraint": location_constraint
                    }
                }
            else:
                location = {}

            Log.logger().debug(">> Trying to create s3 bucket %s.", cls.BUCKET_NAME)
            # import ipdb; ipdb.set_trace(context=5)
            client.create_bucket(Bucket=cls.BUCKET_NAME, **location)
            waiter = client.get_waiter("bucket_exists")
            waiter.wait(Bucket=cls.BUCKET_NAME)
            Log.logger().debug(">> S3 bucket %s exists.", cls.BUCKET_NAME)

            return cls.BUCKET_NAME
        except BaseException as err:
            Log.logger().debug(
                ">> Failed to create s3 bucket %s. Error: %s.", cls.BUCKET_NAME, err
            )
            return cls.BUCKET_NAME

    @classmethod
    def delete_bucket(cls, profile: str) -> Dict[str, Union[str, bool]]:
        client = cls.s3client(profile=profile, aws_region="us-east-1")
        client.delete_bucket(Bucket=cls.BUCKET_NAME)
        waiter = client.get_waiter("bucket_not_exists")
        waiter.wait(Bucket=cls.BUCKET_NAME)

        return {"s3bucket": cls.BUCKET_NAME, "exists": False}

    @classmethod
    def create_table(
        cls, name: str, profile: str, region: Union[str, None] = None
    ) -> Union[str, None]:
        if region is None:
            location = {}
        else:
            location = {"aws_region": region}

        try:
            client = cls.dynamodb_client(profile=profile, **location)
            table = client.create_table(
                TableName=name,
                KeySchema=[{"AttributeName": "LockID", "KeyType": "HASH"}],
                AttributeDefinitions=[
                    {"AttributeName": "LockID", "AttributeType": "S"}
                ],
                BillingMode="PAY_PER_REQUEST",
            )
            if table:
                waiter = client.get_waiter("table_exists")
                waiter.wait(TableName=name)
            return name
        except ClientError as err:
            Log.logger().debug(">> Can't create table %s. Error: %s.", name, err)
            response = err.response["Error"]["Code"]
            if response == "ResourceInUseException":
                Log.logger().debug(
                    ">> Table '%s' already exists. INFO: %s.", name, response
                )
                return name

            Log.logger().debug(
                ">> Client error occurred while creating table '%s'. ERROR: %s.",
                name,
                response,
            )
            return None

    @classmethod
    def delete_table(
        cls, name: str, profile: str, region: str
    ) -> Dict[str, Union[str, bool]]:
        client = cls.dynamodb_client(profile=profile, aws_region=region)
        client.delete_table(TableName=name)
        waiter = client.get_waiter("table_not_exists")
        waiter.wait(TableName=name)

        return {"dynamodb_table": name, "exists": False}

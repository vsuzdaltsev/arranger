from eusy_automation_aws.basic_resource import BasicAwsResource
from eusy_automation_aws.client import AwsClient


class LambdaHelper(BasicAwsResource):
    def __init__(self, boto_client: type(AwsClient)):
        super().__init__(boto_client=boto_client)

    def lambda_edge_highest_num_version_arn(self, name):
        list_versions = self.client.list_versions_by_function(FunctionName=name)
        version_arns = []
        if len(list_versions["Versions"]) == 1:
            raise f"No Numbered version exists for Lambda {name}. Publish lambda function!!"
        else:
            for version in list_versions["Versions"]:
                if version["Version"] != "$LATEST":
                    version_arns.append(version["FunctionArn"])

            return max(version_arns)


if __name__ == "__main__":
    client = AwsClient(
        name="lambda", region="us-east-1", aws_profile="WS-015M-role_AUTOMATION"
    ).client
    result = LambdaHelper(boto_client=client).lambda_edge_highest_num_version_arn(
        name="redirect-cloudfront-url-lambda"
    )
    print(result)

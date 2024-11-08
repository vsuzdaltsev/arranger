from ._basic_build_and_push_image_to_ecr import (
    BasicBuildAndPushImageToEcrBack,
    BasicBuildAndPushImageToEcrFront,
)


class MultiPlatformBuildAndPushImageToEcrBack(BasicBuildAndPushImageToEcrBack):
    pass


class MultiPlatformBuildAndPushImageToEcrFront(BasicBuildAndPushImageToEcrFront):
    pass


if __name__ == "__main__":
    from arranger_automation_aws.ecr import EcrAccessCredentials

    docker_credentials = [
        EcrAccessCredentials(cluster_name_alias="develop1").ecr_access_credentials()
    ]

    params = {
        "cluster_name_alias": "develop1",
        "mvn": {
            "package": "bank-gate-ms",
            "namespace": "com.mydomain.myproject",
            "package_version": "0.0.1-SNAPSHOT",
            "create_ecr_repo": True,
        },
        "image_name": "bank-gate-ms",
        "tag": "latest",
        "additional_tags": "d7,test",
        "debug": True,
        "cleanup": True,
        "build_args": {"JAR_PATH": "default.jar"},
    }
    print(
        MultiPlatformBuildAndPushImageToEcrBack(**params).run(
            docker_credentials=docker_credentials
        )
    )

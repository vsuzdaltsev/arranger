from arranger_cdktf.imports.aws.iam_user import IamUser

from .basic_stack import AwsBasicStack, Construct, TfConf


class DemoIamUserStack(AwsBasicStack):
    """
    Demo stack.
    Create Demo AWS IAM user.
    """

    @property
    def _name_prefix(self) -> str:
        return "test-user"

    def __init__(self, scope: Construct, ns: str, config: TfConf):
        super().__init__(scope, ns, config=config)

        self.aws_provider = self.globals.automation(scope=self)

        self.test_user = self._test_user()

    def _test_user(self) -> IamUser:
        name = self._name(object_type="test-user")

        return IamUser(
            scope=self,
            id_=name,
            name=name,
            provider=self.aws_provider,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
        )


class Development1DemoIamUserStack(DemoIamUserStack):
    """
    Demo stack.
    Development1 tenant version.
    """

    def _test_user(self) -> IamUser:
        name = self._name(object_type="test-user")

        return IamUser(
            scope=self,
            id_=name,
            name=name,
            provider=self.aws_provider,
            tags=self.stack_tags | {"for development1 tenant only": "true"},
            lifecycle=self.lifecycle_policy(),
        )

# AWS public cloud

## Configure AWS credentials

By default, Arranger Invoke tasks utilize AWS profiles, which can be configured as described in the AWS documentation [here](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html).

```shell
# Example of an Invoke task that points to a specific profile, which shares the same name as the tenant.
$ inv tf.diff -p tf --tenant development1 --stack acm-stack
```
where `tenant` is the name of a proper `AWS profile`

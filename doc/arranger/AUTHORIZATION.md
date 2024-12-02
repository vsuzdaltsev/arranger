# AWS public cloud

## Configure AWS credentials

By default, Arranger Invoke tasks utilize AWS profiles, which can be configured as described in the AWS documentation [here](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html).

When the Arranger container starts, the local ~/.aws directory is mounted to the corresponding directory within the container. 
This setup ensures that AWS profiles are accessible from within the container.

`Note`: It is important to ensure that the AWS credentials are correctly configured in the local ~/.aws directory to avoid any access issues.

Example of an Invoke task that points to a specific profile, which shares the same name as the tenant.

```shell
(arranger) root@cli#  inv tf.diff --tenant development1 --stack acm-stack
```
where `tenant` is the name of a proper `AWS profile`

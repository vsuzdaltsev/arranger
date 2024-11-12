# AWS public cloud

## Configure AWS credentials

By default Invoke tasks use AWS profiles https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html

```shell
$ inv tf.diff -p tf --tenant development1 --stack acm-stack
```
where `tenant` is the name of a proper `AWS profile`

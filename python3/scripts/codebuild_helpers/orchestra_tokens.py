"""
This script generates command for issuing sts tokens
    for each of the existing AWS accounts except Orchestra.
    :param 1 - where library
    :param 2 - select given cluster.

It is used within Codebuild pipelines of the orchestrating account for getting access to all other accounts.

python python3/scripts/codebuild_helpers/orchestra_tokens.py python3/packages switchdev1
>>
issue_sts_token 091969078577 switchdev1;


python python3/scripts/codebuild_helpers/orchestra_tokens.py python3/packages
>>
...
issue_sts_token 724906484045 sandbox1;
issue_sts_token 091969078577 switchdev1;
"""

import glob
import os
import sys

where_lib = sys.argv[1]


def select_cluster():
    if len(sys.argv) > 2:
        return sys.argv[2]

    return None


os.chdir(where_lib)

for module in glob.glob("*/eusy_conf"):
    sys.path.append(module)

import app_conf


def _output(metadata):
    account_name_pattern = metadata.get("aws_profile")
    print(f"issue_sts_token {metadata.get('aws_account_id')} {account_name_pattern};")


for cluster, _metadata in app_conf.AppConf.CLUSTERS.items():
    if select_cluster() in app_conf.AppConf.ORCHESTRA_SUBORDINATE_ACCOUNTS:
        if select_cluster() == cluster:
            _output(metadata=_metadata)
    else:
        if cluster in app_conf.AppConf.ORCHESTRA_SUBORDINATE_ACCOUNTS:
            _output(metadata=_metadata)

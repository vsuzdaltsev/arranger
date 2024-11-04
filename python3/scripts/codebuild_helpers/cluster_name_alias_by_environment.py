"""
This script generates a map 'environment'=>'cluster_name-alias' for given environment.
    $ python python3/scripts/codebuild_helpers/cluster_name_alias_by_environment.py python3/packages d1 | jq

Example output:
>>
...
{
  "d1": "switchdev1"
}
"""

import glob
import json
import os
import sys

where_lib = sys.argv[1]
environment = sys.argv[2]
os.chdir(where_lib)

for module in glob.glob("*/eusy_conf"):
    sys.path.append(module)

import app_conf


for cluster, metadata in app_conf.AppConf.CLUSTERS.items():
    if metadata and metadata.get("sub_environments"):
        if environment in metadata.get("sub_environments"):
            print(json.dumps({environment: cluster}))

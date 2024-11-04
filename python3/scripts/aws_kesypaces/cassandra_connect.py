import json
import os

from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider

from eusy_automation_aws.sm import SecretsManagerItem

# contact_points = ["vpce-04939acc8b74bb3b0-gll481dx.cassandra.eu-west-2.vpce.amazonaws.com"]
contact_points = ["cassandra.eu-west-2.amazonaws.com"]


os.system("curl https://certs.secureserver.net/repository/sf-class2-root.crt -O")
secret = SecretsManagerItem(
    secret_name="switchdev1/bank-gate-ms", aws_profile="switchdev1"
).retrieve()
keyspace = "bank_gate_ms_d1_switchdev1"
password = secret["CASSANDRA_PASSWORD"]
username = secret["CASSANDRA_USERNAME"]


ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.load_verify_locations("sf-class2-root.crt")
ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(
    contact_points, ssl_context=ssl_context, auth_provider=auth_provider, port=9142
)
session = cluster.connect()

create_table_query = """
    CREATE TABLE IF NOT EXISTS bank_gate_ms_d1_switchdev1.test_table (
        id UUID PRIMARY KEY,
        name TEXT
    )
"""


r = session.execute(create_table_query)
print(json.dumps(r.current_rows, default=str))

#!/bin/bash

echo "--- Creating certificates directory----------------------------------------------------------------"
mkdir -p certificates
cd certificates

client_name="MB03KE20"

# echo "--- Generate private Certificate Authority (CA) private key ---------------------------------------"
# openssl genrsa -out root-ca.key 4096

# echo "--- Generate private CA public key ----------------------------------------------------------------"
# echo "(Keep all properties besides Common Name empty. Use 'rootca' for common name.)"
# openssl req -new -x509 -days 3650 -key root-ca.key -out root-ca.pem

echo "--- Generate private client key -------------------------------------------------------------------"
openssl genrsa -out client.${client_name}.key 2048

echo "--- Generate a certificate signing request (CSR) for the private client key -----------------------"
echo "(Keep all properties besides Common Name empty. Use 'client1' for common name. Keep password empty)"
openssl req -new -key client.${client_name}.key -out client.${client_name}.csr

echo "--- Sign the private client (CSR) with the private CA created earlier -----------------------------"
openssl x509 -req -in client.${client_name}.csr -CA root-ca.pem -CAkey root-ca.key -set_serial 01 -out client.${client_name}.pem -days 3650 -sha256

echo "--- Create a Trust Store --------------------------------------------------------------------------"
cp root-ca.pem ../src/upload-truststore/truststore.pem

echo "--- Done ------------------------------------------------------------------------------------------"
# echo "API Gateway is configured to use this truststore as part of "
# echo "This will be done as part of running the CloudFormation/SAM template."
# api-gateway-certificate-propagation % aws s3 cp certificates/truststore.pem s3://api-gateway-certificate-propagat-truststorebucket-ygnryqp0p6fd/truststore.pem

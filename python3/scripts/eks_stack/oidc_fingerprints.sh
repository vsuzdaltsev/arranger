#!/bin/bash

# Get EKS OIDC endpoint certificate fingerprint to use it while creating OIDC provider for the EKS cluster.
# The script extracts only the last cert in the chain. Please see EKS stack for the details.
# Openssl package needs to be installed in order to run this script.
# Example usage:
#  bash python3/scripts/eks_stack/oidc_fingerprints.sh eu-west-2 | jq

command -v openssl > /dev/null || exit 1

aws_region=$1

if [[ $aws_region == "" ]] ; then
  builtin echo -e ">> First parameter should be an AWS region. You passed none.."
  exit 1
fi

temp_dir=$(mktemp -d)
server="oidc.eks".${aws_region}."amazonaws.com:443"

openssl s_client -showcerts -verify 5 -connect "${server}" 2>/dev/null < /dev/null |
 awk '/BEGIN CERTIFICATE/,/END CERTIFICATE/{ if(/BEGIN CERTIFICATE/){a++}; out="'"${temp_dir}"'/cert"a".pem"; print >out}'

for crt in "${temp_dir}"/cert[[:digit:]].pem ; do
  fingerprint=$(openssl x509 -noout -fingerprint -sha1 -in ${crt} | cut -d "=" -f 2 | tr -d ":" |
   tr '[:upper:]' '[:lower:]')
done

echo -e '{"FINGERPRINT": '\""${fingerprint}"\"'}'

trap 'rm -rf -- "'"${temp_dir}"'"' EXIT

exit 0

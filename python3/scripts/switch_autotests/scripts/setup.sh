#!/bin/bash

echo ">> MY EXTERNAL IP FROM EC2: $(curl -s https://2ip.ru)"

systemctl restart snapd.seeded.service

sudo snap install aws-cli --classic > /dev/null
#sudo snap install openjdk > /dev/null
pwd

sudo wget https://download.java.net/java/GA/jdk20.0.2/6e380f22cbe7469fa75fb448bd903d8e/9/GPL/openjdk-20.0.2_linux-x64_bin.tar.gz
sudo tar -xvf openjdk-20.0.2_linux-x64_bin.tar.gz
sudo mkdir -p /usr/local/openjdk-20
cd jdk-20.0.2/
sudo mv * /usr/local/openjdk-20
sudo ln -s /usr/local/openjdk-20/bin/java /usr/bin/java
sudo java --version

sudo wget https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_amd64 -O ./allurectl

sudo chmod +x ./allurectl
sudo mv ./allurectl /bin/

sudo apt-get update > /dev/null
sudo apt-get install resolvconf maven -y > /dev/null

sudo -E mkdir -p /home/ubuntu/.aws
sudo -E cp -av /home/ubuntu/aws_credentials /home/ubuntu/.aws/credentials
sudo -E sudo curl -fL https://app.getambassador.io/download/tel2oss/releases/download/v2.15.1/telepresence-linux-amd64 -o /usr/local/bin/telepresence
sudo -E chmod a+x /usr/local/bin/telepresence

exit 0

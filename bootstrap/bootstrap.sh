#!/usr/bin/env bash

apt-get update
apt-get install -y curl
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
apt-get install -y nodejs python3-venv python-pip python3-pip unzip
update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
npm install -g aws-cdk
python -m pip install aws-cdk.aws-lambda aws-cdk.aws-iam
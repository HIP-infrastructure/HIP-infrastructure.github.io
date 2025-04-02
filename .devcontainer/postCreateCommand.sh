#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-sphinx
pip3 install -r /workspaces/HIP-infrastructure.github.io/requirements.txt
sudo apt-get install -y git
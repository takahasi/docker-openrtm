#!/bin/bash

install="sudo apt-get install -y"
update="sudo apt-get update -qq"
remove="sudo apt-get remove -y"
key="sudo apt-key"
add_repo="sudo add-apt-repository"
repo="[arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#repo="[arch=armhf] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Remove old version
$remove docker docker-engine docker.io

# Install base package
$update
$install linux-image-extra-$(uname -r) linux-image-extra-virtual
$install apt-transport-https ca-certificates curl software-properties-common

# Setup Docker repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$key fingerprint 0EBFCD88
$add_repo $repo

# Install Docker
$update
$install docker-ce

# Setup permission
sudo groupadd docker
sudo gpasswd -a $USER docker

echo "Please reboot to reflect this change."

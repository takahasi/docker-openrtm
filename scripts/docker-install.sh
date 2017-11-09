#!/bin/bash

set -ue

# Docker Official Repository
version=`lsb_release -cs`
repo="deb [arch=amd64] https://download.docker.com/linux/ubuntu $version stable"
#repo="[arch=armhf] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Docker Packages
packages_docker_old="docker docker-engine docker.io"
packages_docker="docker-ce"
packages_extra="linux-image-extra-$(uname -r) \
    linux-image-extra-virtual \
    apt-transport-https ca-certificates \
    curl \
    software-properties-common"

# Commands
su="sudo"
apt="$su apt-get"
install="$apt install -y"
update="$apt update -qq"

function preinstall() {
  # Remove old version
  $apt remove -y $packages_docker_old

  # Install base package
  $update
  $install $packages_extra
}

function install() {
  # Setup Docker repository
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  $su apt-key fingerprint 0EBFCD88
  $su add-apt-repository "$repo"

  # Install Docker
  $update
  $install $packages_docker
}

function setup() {
  # Setup permission
  if $su groupadd docker > /dev/null
  then
    $su gpasswd -a $USER docker
    echo "Please reboot or re-login to reflect this change."
  fi
}

preinstall
install
setup

exit 0

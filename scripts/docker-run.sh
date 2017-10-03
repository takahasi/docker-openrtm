#!/bin/bash

set -ue

# Docker Hub Image
DH_USER=takahasi
DH_REPO=docker-openrtm
TAG=ubuntu1604_openrtm112-desktop
IMAGE=$DH_USER/$DH_REPO:$TAG

# Docker Option
NET_OPT="--net=host"
X_OPT="-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority"

# Enable X11-forwarding
xhost local:

# Start docker w/X11-forwarding
docker run -ti --rm $X_OPT $NET_OPT $IMAGE -c bash

# Disable X11-forwarding
xhost -

exit 0

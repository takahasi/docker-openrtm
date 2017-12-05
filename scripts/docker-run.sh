#!/bin/bash

set -e

# TAG NAME
if [ $1=="" ];then
  tag="latest"
else
  tag=$1
fi

# Docker Hub Image
DH_USER=takahasi
DH_REPO=docker-openrtm

image=$DH_USER/$DH_REPO:$tag
echo "IMAGE: $image"

# Docker Option
entry=$PWD
option="-v $HOME:$HOME:rw --privileged=true -e ENTRY=$entry"
option_network="--net=host"
option_display="-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority"

# Enable X11-forwarding
xhost local:

# Start docker w/X11-forwarding
docker run -ti --rm $option $option_display $option_network $image -c 'cd $ENTRY;bash'

# Disable X11-forwarding
xhost -

exit 0

#!/bin/bash

set -e

# TAG NAME
# tag=ubuntu1604_openrtm112-desktop
tag=$1

# Docker Hub Image
DH_USER=takahasi
DH_REPO=docker-openrtm

if [ $tag=="" ];then
  image=$DH_USER/$DH_REPO
else
  image=$DH_USER/$DH_REPO:$tag
fi
echo "IMAGE: $tag"

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

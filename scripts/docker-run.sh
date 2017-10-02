#!/bin/bash

IMAGE=takahasi/docker-openrtm:ubuntu1604_openrtm112-desktop
NETWORK=host
X_OPT="-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority"

# Enable X11-forwarding
xhost local:

# Start docker w/X11-forwarding
docker run -ti --rm $X_OPT--net=$NETWORK $IMAGE -c bash

# Disable X11-forwarding
xhost -

exit 0

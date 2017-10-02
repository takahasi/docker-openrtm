#!/bin/bash

IMAGE=takahasi/docker-openrtm:ubuntu1604_openrtm112-desktop
NETWORK=host
X_OPT="-e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority"

docker run -ti --rm $X_OPT--net=$NETWORK $IMAGE -c bash

#!/bin/bash

IMAGE=takahasi/docker-openrtm:ubuntu1604_openrtm112

docker run -ti --rm -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $HOME/.Xauthority:/root/.Xauthority --net=host \
    $IMAGE -c bash

#!/bin/bash

# stop & remove all docker images
docker stop `docker ps -a -q`
docker rm -f `docker ps -a -q`
docker rmi -f `docker images -a -q`

exit 0

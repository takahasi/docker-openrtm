#!/bin/bash

set -ue

# stop & remove all docker images
docker stop `docker ps -a -q`
docker rm `docker ps -a -q`
docker rmi `docker images -a -q`

exit 0

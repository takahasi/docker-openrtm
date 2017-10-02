#!/bin/bash

purge="sudo apt-get purge -y"

$purge docker-ce
sudo rm -rf /var/lib/docker

echo "Please reboot to reflect this change."

exit 0

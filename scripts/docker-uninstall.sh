#!/bin/bash

set -ue

sudo apt-get purge -y docker-ce
sudo rm -rf /var/lib/docker

echo "Please reboot to reflect this change."

exit 0

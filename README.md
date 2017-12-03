OpenRTM on Docker (docker-openrtm)
==================================
Docker images of OpenRTM-aist.
Please check [manual.](https://readthedocs.org/projects/openrtm-on-docker/)

# Build Status

[![TextLint by Travis.ci Status](https://travis-ci.org/takahasi/docker-openrtm.svg?branch=master)](https://travis-ci.org/takahasi/docker-openrtm)

[![Documentation by Read the Docs Status](https://readthedocs.org/projects/openrtm-on-docker/badge/?version=latest)](http://openrtm-on-docker.readthedocs.io/ja/latest/?badge=latest)


# Usage
If you try these images, just type the below;

`docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash`

If you customize based on these imases,
please add the below in your Dockerfile;

`FROM takahasi/docker-openrtm:ubuntu1404_openrtm112`

If you use desktop version, you can connect container via RDP protocol.
(default user:root, password:root)

Or you can use X-window forwarding(Linux only);

`wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-run.sh
chmod +x docker-run.sh
./script/docker-run.sh`


# Docker Hub
https://hub.docker.com/r/takahasi/docker-openrtm/

# OpenRTM-aist
http://www.openrtm.org/openrtm/

# Dockerfile github
https://github.com/takahasi/docker-openrtm

# Document
http://openrtm-on-docker.readthedocs.io/ja/latest/


# Image List

Please check [OpenRTM on Docker Web Page](https://takahasi.github.io/docker-openrtm/) to get detail information.

- latest (ubuntu1604_openrtm112-desktop)
- ubuntu1204_openrtm112-desktop
- ubuntu1404_openrtm112-desktop
- ubuntu1604_openrtm112-desktop
- ubuntu1610_openrtm112-desktop
- ubuntu1704_openrtm112-desktop
- ubuntu1204_openrtm112
- ubuntu1404_openrtm112
- ubuntu1604_openrtm112
- ubuntu1610_openrtm112
- ubuntu1704_openrtm112
- ubuntu1204_openrtm112-cxx
- ubuntu1404_openrtm112-cxx
- ubuntu1604_openrtm112-cxx
- ubuntu1610_openrtm112-cxx
- ubuntu1704_openrtm112-cxx
- ubuntu1204_openrtm112-python
- ubuntu1404_openrtm112-python
- ubuntu1604_openrtm112-python
- ubuntu1610_openrtm112-python
- ubuntu1704_openrtm112-python
- fedora24_openrtm112
- fedora25_openrtm112
- debian8_openrtm112
- debian9_openrtm112
- ubuntu1204_openrtm120-desktop
- ubuntu1404_openrtm120-desktop
- ubuntu1604_openrtm120-desktop
- ubuntu1610_openrtm120-desktop
- ubuntu1704_openrtm120-desktop
- ubuntu1204_openrtm120
- ubuntu1404_openrtm120
- ubuntu1604_openrtm120
- ubuntu1610_openrtm120
- ubuntu1704_openrtm120
- ubuntu1204_openrtm120-cxx
- ubuntu1404_openrtm120-cxx
- ubuntu1604_openrtm120-cxx
- ubuntu1610_openrtm120-cxx
- ubuntu1704_openrtm120-cxx
- ubuntu1204_openrtm120-python
- ubuntu1404_openrtm120-python
- ubuntu1604_openrtm120-python
- ubuntu1610_openrtm120-python
- ubuntu1704_openrtm120-python
- ubuntu1204_openrtm120-java
- ubuntu1404_openrtm120-java
- ubuntu1604_openrtm120-java
- ubuntu1610_openrtm120-java
- ubuntu1704_openrtm120-java

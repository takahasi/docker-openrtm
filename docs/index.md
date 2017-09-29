docker-openrtm
==============
Docker images for OpenRTM-aist

# Usage
If you try these images temporary;

`docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash`

If you customize based on these imases,
please add the below in your Dockerfile;

`FROM takahasi/docker-openrtm:ubuntu1404_openrtm112`

If you use desktop version, you can connect container via RDP protocol.
(default user:root, password:root)


# Docker Hub
https://hub.docker.com/r/takahasi/docker-openrtm/

# OpenRTM-aist
http://www.openrtm.org/openrtm/

# Dockerfile github
https://github.com/takahasi/docker-openrtm

# Image List
## Latest
|Tag|RTM|OS|cxx|python|java|rtshell|openrtp|desktop(rdp)|Status|
|---|---|--|---|------|----|-------|-------|------|
|latest|1.2.0|ubuntu 16.04 64bit|O|O|O|O|O|O|OK|

## OpenRTM-aist 1.1.2
|Tag|OS|cxx|python|java|rtshell|openrtp|desktop(rdp)|Status|
|---|--|---|------|----|-------|-------|------------|------|
|ubuntu1204_openrtm112-desktop|ubuntu 12.04 64bit|O|O|O|O|O|O|OK|
|ubuntu1404_openrtm112-desktop|ubuntu 14.04 64bit|O|O|O|O|O|O|OK|
|ubuntu1604_openrtm112-desktop|ubuntu 16.04 64bit|O|O|O|O|O|O|OK|
|ubuntu1610_openrtm112-desktop|ubuntu 16.10 64bit|O|O|O|O|O|O|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1704_openrtm112-desktop|ubuntu 17.04 64bit|O|O|O|O|O|O|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1204_openrtm112|ubuntu 12.04 64bit|O|O|O|O|O|-|OK|
|ubuntu1404_openrtm112|ubuntu 14.04 64bit|O|O|O|O|O|-|OK|
|ubuntu1604_openrtm112|ubuntu 16.04 64bit|O|O|O|O|O|-|OK|
|ubuntu1610_openrtm112|ubuntu 16.10 64bit|O|O|O|O|O|-|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1704_openrtm112|ubuntu 17.04 64bit|O|O|O|O|O|-|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1204_openrtm112-cxx|ubuntu 12.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1404_openrtm112-cxx|ubuntu 14.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1604_openrtm112-cxx|ubuntu 16.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1610_openrtm112-cxx|ubuntu 16.10 64bit|O|-|-|-|-|-|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1704_openrtm112-cxx|ubuntu 17.04 64bit|O|-|-|-|-|-|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1204_openrtm112-python|ubuntu 12.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1404_openrtm112-python|ubuntu 14.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1604_openrtm112-python|ubuntu 16.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1610_openrtm112-python|ubuntu 16.10 64bit|-|O|-|-|-|-|N/A, OpenRTM-aist-1.1.2 is not support|
|ubuntu1704_openrtm112-python|ubuntu 17.04 64bit|-|O|-|-|-|-|N/A, OpenRTM-aist-1.1.2 is not support|
|fedora24_openrtm112|fedora 24 64bit|O|O|O|O|O|-|N/A, OpenRTM-aist-1.1.2 is not support|
|fedora25_openrtm112|fedora 25 64bit|O|O|O|O|O|-|N/A, OpenRTM-aist-1.1.2 is not support|
|debian8_openrtm112|debian 8 64bit|O|O|O|O|O|-|N/A, OpenRTM-aist-1.1.2 is not support|
|debian9_openrtm112|debian 9 64bit|O|O|O|O|O|-|N/A, OpenRTM-aist-1.1.2 is not support|

## OpenRTM-aist 1.2.0
|Tag|OS|cxx|python|java|rtshell|openrtp|desktop(rdp)|Status|
|---|--|---|------|----|-------|-------|------------|------|
|ubuntu1204_openrtm120|ubuntu 12.04 64bit|O|O|O|O|O|-|N/A, rtshell is not support|
|ubuntu1404_openrtm120|ubuntu 14.04 64bit|O|O|O|O|O|-|OK|
|ubuntu1604_openrtm120|ubuntu 16.04 64bit|O|O|O|O|O|-|OK|
|ubuntu1610_openrtm120|ubuntu 16.10 64bit|O|O|O|O|O|-|OK|
|ubuntu1704_openrtm120|ubuntu 17.04 64bit|O|O|O|O|O|-|OK|
|ubuntu1204_openrtm120-cxx|ubuntu 12.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1404_openrtm120-cxx|ubuntu 14.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1604_openrtm120-cxx|ubuntu 16.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1610_openrtm120-cxx|ubuntu 16.10 64bit|O|-|-|-|-|-|OK|
|ubuntu1704_openrtm120-cxx|ubuntu 17.04 64bit|O|-|-|-|-|-|OK|
|ubuntu1204_openrtm120-python|ubuntu 12.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1404_openrtm120-python|ubuntu 14.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1604_openrtm120-python|ubuntu 16.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1610_openrtm120-python|ubuntu 16.10 64bit|-|O|-|-|-|-|OK|
|ubuntu1704_openrtm120-python|ubuntu 17.04 64bit|-|O|-|-|-|-|OK|
|ubuntu1204_openrtm120-java|ubuntu 12.04 64bit|-|-|O|-|-|-|OK|
|ubuntu1404_openrtm120-java|ubuntu 14.04 64bit|-|-|O|-|-|-|OK|
|ubuntu1604_openrtm120-java|ubuntu 16.04 64bit|-|-|O|-|-|-|OK|
|ubuntu1610_openrtm120-java|ubuntu 16.10 64bit|-|-|O|-|-|-|OK|
|ubuntu1704_openrtm120-java|ubuntu 17.04 64bit|-|-|O|-|-|-|OK|


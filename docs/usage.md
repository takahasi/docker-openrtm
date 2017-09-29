Usage
=====
Please try;

`docker run --rm -ti takahasi/docker-openrtm bash`

If you want to select version;

`docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash`

If you customize based on these imases,
please add the below in your Dockerfile;

`FROM takahasi/docker-openrtm:ubuntu1404_openrtm112`

If you use desktop version, you can connect container via RDP protocol.
(default user:root, password:root)

![Docker for OpenRTM as a Development Environment](img/sample1.png)

![Docker for OpenRTM as a Verification Environment](img/sample2.png)

[Top Page](index)

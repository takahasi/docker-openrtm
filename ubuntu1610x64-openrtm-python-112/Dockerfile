
FROM ubuntu:16.10
MAINTAINER takahasi <3263ta@gmail.com>

ENV dist ubuntu
ENV rtmver 1_1_2
ENV DEBIAN_FRONTEND noninteractive


RUN set -x && \
    alias apt-get='apt-get -y' && \
    apt-get -qq update && \
    apt-get install -y curl bc python-pip bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \
    chmod a+x pkg_install_python_${dist}.sh && \
    ./pkg_install_python_${dist}.sh -y && \
    apt-get autoclean && \
    apt-get autoremove


ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

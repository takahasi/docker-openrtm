
FROM ubuntu:16.10
MAINTAINER takahasi <3263ta@gmail.com>

ENV dist ubuntu
ENV rtmver 1_1_2
ENV DEBIAN_FRONTEND noninteractive


RUN set -x && \
    apt-get -qq update && \
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    ./pkg_install_${dist}.sh -c && \
    apt-get autoclean -y && \
    apt-get autoremove -y


ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

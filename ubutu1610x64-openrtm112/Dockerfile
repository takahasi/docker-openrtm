FROM ubuntu:16.10
MAINTAINER takahasi

ENV dist="ubuntu"
ENV distver="16.10"
ENV rtmver="1_1_2"
RUN set -x && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes curl && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    bash ./pkg_install_${dist}.sh

ENTRYPOINT ["/bin/bash", "-c"]

EXPOSE 80

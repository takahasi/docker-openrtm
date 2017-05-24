
FROM ubuntu:17.04
MAINTAINER takahasi

ENV dist=ubuntu
ENV rtmver=1_1_1
RUN set -x && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes curl bc && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    ./pkg_install_${dist}.sh -s

ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

FROM ubuntu:17.04

RUN set -x
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes curl && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_ubuntu.sh && \
    chmod a+x pkg_install_ubuntu.sh && \
    ./pkg_install_ubuntu.sh -s

ENTRYPOINT ["/bin/bash", "-c"]

EXPOSE 80

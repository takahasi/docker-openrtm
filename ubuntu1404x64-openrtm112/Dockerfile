
FROM ubuntu:14.04
MAINTAINER takahasi

ENV dist=ubuntu
ENV rtmver=1_1_2
RUN set -x && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes curl bc default-jre python-pip && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    ./pkg_install_${dist}.sh -c && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh && \
    chmod a+x pkg_install_python_ubuntu.sh && \
    ./pkg_install_python_ubuntu.sh -y && \
    pip install rtshell && \
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    cp eclipse/openrtp /usr/bin/

ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

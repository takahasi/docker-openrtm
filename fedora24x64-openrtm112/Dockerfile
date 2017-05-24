
FROM fedora:24
MAINTAINER takahasi

ENV dist=fedora
ENV rtmver=1_1_2
RUN set -x && \
    alias dnf='dnf -y' && \
    dnf install -y curl bc python-pip java-1.8.0-openjdk-headless && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    ./pkg_install_${dist}.sh -c && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \
    chmod a+x pkg_install_python_${dist}.sh && \
    ./pkg_install_python_${dist}.sh -y && \
    pip install -U pip && \
    pip install rtshell && \
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    ln -s /usr/share/openrtm-1.1/eclipse/openrtp /usr/bin/ && \
    rtm-naming

ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

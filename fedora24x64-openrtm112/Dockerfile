
FROM fedora:24
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="fedora-all"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && dnf update -qq

RUN dnf install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    dnf install -y python-pip && \
    dnf install -y default-jre && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_fedora.sh && \
    chmod a+x pkg_install_fedora.sh && sync && \
    ./pkg_install_fedora.sh -c && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_fedora.sh && \
    chmod a+x pkg_install_python_fedora.sh && sync && \
    ./pkg_install_python_fedora.sh -y && \
    pip install -U pip && \
    pip install rtshell && \
    mkdir -p /etc/bash_completion.d/ && \
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    ln -s /eclipse/openrtp /usr/bin/ && \
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr.. && make install && cd /

RUN dnf autoclean -y && dnf autoremove -y

ENTRYPOINT ["/bin/bash", "-c"]

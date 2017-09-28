
FROM ubuntu:14.04
MAINTAINER takahasi <3263ta@gmail.com>

ENV dist ubuntu
ENV rtmver 1_1_2
ENV DEBIAN_FRONTEND noninteractive


RUN set -x && \
    alias apt-get='apt-get -y' && \
    apt-get -qq update && \
    apt-get install -y curl bc default-jre python-pip bsdmainutils apt-utils aptitude iputils-ping net-tools lxde xrdp && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    ./pkg_install_${dist}.sh -c && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \
    chmod a+x pkg_install_python_${dist}.sh && \
    ./pkg_install_python_${dist}.sh -y && \
    pip install -U pip && \
    pip install rtshell && \
    mkdir -p /etc/bash_completion.d/ && \
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    ln -s /eclipse/openrtp /usr/bin/ && \
    apt-get clean && \
    apt-get autoremove && \
    RUN passwd -d root


ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

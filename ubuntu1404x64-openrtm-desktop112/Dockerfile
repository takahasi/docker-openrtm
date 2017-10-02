
FROM ubuntu:14.04
LABEL maintainer=takahasi <3263ta@gmail.com> \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images."

ENV dist ubuntu
ENV rtmver 1_1_2
ENV DEBIAN_FRONTEND noninteractive


RUN set -x && \
    apt-get -qq update && \
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    apt-get install -y python-pip && \
    apt-get install -y default-jre && \
    apt-get install -y lxde xrdp && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \
    chmod a+x pkg_install_${dist}.sh && \
    sync && \
    ./pkg_install_${dist}.sh -c && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \
    chmod a+x pkg_install_python_${dist}.sh && \
    sync && \
    ./pkg_install_python_${dist}.sh -y && \
    pip install -U pip && \
    pip install rtshell && \
    mkdir -p /etc/bash_completion.d/ && \
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    ln -s /eclipse/openrtp /usr/bin/ && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    yes root | passwd root


CMD ["/etc/init.d/xvnc", "start"]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

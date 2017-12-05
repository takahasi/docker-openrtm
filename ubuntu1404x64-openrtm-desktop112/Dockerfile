
FROM ubuntu:14.04
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="ubuntu-all_desktop"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq

RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    apt-get install -y python-pip && \
    apt-get install -y default-jre && \
    apt-get install -y lxde xrdp sysv-rc-conf && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_ubuntu.sh && \
    chmod a+x pkg_install_ubuntu.sh && sync && \
    ./pkg_install_ubuntu.sh -c && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh && \
    chmod a+x pkg_install_python_ubuntu.sh && sync && \
    ./pkg_install_python_ubuntu.sh -y && \
    pip install -U pip && \
    pip install rtshell && \
    mkdir -p /etc/bash_completion.d/ && \
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \
    ln -s /eclipse/openrtp /usr/bin/ && \
    echo lxsession -s LXDE -e LXDE > ~/.xsession && \
    sysv-rc-conf xrdp on && \
    yes root | passwd root

CMD ["/etc/init.d/xvnc", "start"]

RUN apt-get autoclean -y && apt-get autoremove -y

CMD ["rtm-naming", ""]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

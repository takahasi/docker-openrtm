
FROM ubuntu:16.10
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images."

ENV dist ubuntu
ENV rtmver 1_1_2
ENV DEBIAN_FRONTEND noninteractive


RUN set -x && \
    apt-get -qq update && \
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    apt-get install -y python-pip && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \
    chmod a+x pkg_install_python_${dist}.sh && \
    sync && \
    ./pkg_install_python_${dist}.sh -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y


CMD ["/etc/init.d/xvnc", "start"]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

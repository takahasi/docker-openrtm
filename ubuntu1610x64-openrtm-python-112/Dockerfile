
FROM ubuntu:16.10
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="ubuntu-python"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq

RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    apt-get install -y python-pip && \
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh && \
    chmod a+x pkg_install_python_ubuntu.sh && sync && \
    ./pkg_install_python_ubuntu.sh -y

RUN apt-get autoclean -y && apt-get autoremove -y

CMD ["/etc/init.d/xvnc", "start"]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

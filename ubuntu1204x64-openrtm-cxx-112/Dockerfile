
FROM ubuntu:12.04
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="ubuntu-cxx"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq

RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_ubuntu.sh && \
    chmod a+x pkg_install_ubuntu.sh && sync && \
    ./pkg_install_ubuntu.sh -c

RUN apt-get autoclean -y && apt-get autoremove -y

CMD ["rtm-naming", ""]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

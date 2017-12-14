
FROM debian:8
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="debian-all"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq

COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools subversion git cmake && \
    apt-get install -y libopencv-dev && \
    chmod a+x ./pkg_install.sh && sync && \
    ./pkg_install.sh -l all -c --yes && \
    ./pkg_install.sh -l all -d --yes && \
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make install && cd /

RUN apt-get autoclean -y && apt-get autoremove -y

ENTRYPOINT ["/bin/bash", "-c"]

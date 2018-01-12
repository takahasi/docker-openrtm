
FROM ubuntu:17.10
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="ubuntu-all_desktop"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && \
    apt-get update -qq

COPY pkg_install.sh /
RUN apt-get install -y bc \
                       cmake \
                       git \
                       iputils-ping \
                       libopencv-dev \
                       lxde \
                       net-tools \
                       python-tk \
                       subversion \
                       xrdp && \
    chmod a+x ./pkg_install.sh && sync && \
    ./pkg_install.sh -l all -c --yes && \
    ./pkg_install.sh -l all -d --yes && \
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make install && cd / && \
    echo lxsession -s LXDE -e LXDE > ~/.xsession && \
    yes root | passwd root


RUN apt-get autoclean -y && \
    apt-get autoremove -y

ENTRYPOINT ["/bin/bash", "-c"]


FROM fedora:25
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="fedora-all_desktop"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && dnf update -y

COPY pkg_install.sh /
RUN dnf install -y bc iputils-ping net-tools subversion git cmake && \
    dnf install -y libopencv-dev && \
    dnf install -y lxde xrdp && \
    dnf install -y python-tk && \
    chmod a+x ./pkg_install.sh && sync && \
    ./pkg_install.sh -l all -c --yes && \
    ./pkg_install.sh -l all -d --yes && \
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make install && cd / && \
    echo lxsession -s LXDE -e LXDE > ~/.xsession && \
    yes root | passwd root

CMD ["/etc/init.d/xvnc", "start"]

RUN dnf autoclean -y && dnf autoremove -y

ENTRYPOINT ["/bin/bash", "-c"]

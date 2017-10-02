
FROM ubuntu:14.04
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="ubuntu-all_desktop"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq

COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools && \
    apt-get install -y lxde xrdp && \
    chmod a+x ./pkg_install.sh && sync && \
    ./pkg_install.sh -l all -c --yes && \
    yes root | passwd root

CMD ["/etc/init.d/xvnc", "start"]

RUN apt-get autoclean -y && apt-get autoremove -y

CMD ["rtm-naming", ""]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

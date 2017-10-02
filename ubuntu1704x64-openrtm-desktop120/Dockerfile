
FROM ubuntu:17.04
LABEL maintainer=takahasi <3263ta@gmail.com> \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images."

ENV dist ubuntu
ENV rtmver 1_2_0
ENV DEBIAN_FRONTEND noninteractive


COPY pkg_install.sh /
RUN set -x && \
    apt-get update -qq && \
    apt-get install -y bc iputils-ping net-tools && \
    apt-get install -y lxde xrdp && \
    chmod a+x ./pkg_install.sh && \
    sync && \
    ./pkg_install.sh -l all -c --yes && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    yes root | passwd root


CMD ["/etc/init.d/xvnc", "start"]
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

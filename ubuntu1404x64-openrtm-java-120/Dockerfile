
FROM ubuntu:14.04
LABEL maintainer="takahasi <3263ta@gmail.com>" \
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \
      build_type="ubuntu-java"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq

COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools && \
    chmod a+x ./pkg_install.sh && sync && \
    ./pkg_install.sh -l java -r --yes

RUN apt-get autoclean -y && apt-get autoremove -y

ENTRYPOINT ["/bin/bash", "-c"]

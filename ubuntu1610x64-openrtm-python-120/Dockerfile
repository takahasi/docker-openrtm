
FROM ubuntu:16.10
MAINTAINER takahasi

ENV DEBIAN_FRONTEND noninteractive
COPY pkg_install.sh /


RUN set -x && \
    apt-get update -qq && \
    apt-get install -y bc iputils-ping net-tools && \
    ./pkg_install.sh -l python -d --yes && \
    apt-get clean


ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

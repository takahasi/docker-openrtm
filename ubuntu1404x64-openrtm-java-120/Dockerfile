
FROM ubuntu:14.04
MAINTAINER takahasi <3263ta@gmail.com>

ENV dist ubuntu
ENV rtmver 1_2_0
ENV DEBIAN_FRONTEND noninteractive


COPY pkg_install.sh /
RUN set -x && \
    apt-get update -qq && \
    apt-get install -y bc iputils-ping net-tools && \
    chmod a+x ./pkg_install.sh && \
    ./pkg_install.sh -l java -r --yes && \
    apt-get autoclean -y && \
    apt-get autoremove -y


ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80

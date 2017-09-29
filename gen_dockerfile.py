#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" script for generate dockerfile templates

This is xxx
"""

import os

dockerfile_template_common_header = '''
FROM @IMAGE_NAME@
MAINTAINER @AUTHOR@

ENV dist @DISTRIBUTION@
ENV rtmver @RTM_VERSION@
ENV DEBIAN_FRONTEND noninteractive

'''

dockerfile_template_common_footer = '''

ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80
'''

dockerfile_template_12x_all_desktop = '''
COPY pkg_install.sh /
RUN set -x && \\
    apt-get update -qq && \\
    apt-get install -y bc iputils-ping net-tools && \\
    apt-get install -y lxde xrdp && \\
    chmod a+x ./pkg_install.sh && \\
    ./pkg_install.sh -l all -c --yes && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y && \\
    RUN passwd -d root
'''

dockerfile_template_12x_all = '''
COPY pkg_install.sh /
RUN set -x && \\
    apt-get update -qq && \\
    apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && \\
    ./pkg_install.sh -l all -c --yes && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''

dockerfile_template_12x_cxx = '''
COPY pkg_install.sh /
RUN set -x && \\
    apt-get update -qq && \\
    apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && \\
    ./pkg_install.sh -l c++ -r --yes && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''

dockerfile_template_12x_python = '''
COPY pkg_install.sh /
RUN set -x && \\
    apt-get update -qq && \\
    apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && \\
    ./pkg_install.sh -l python -r --yes && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''

dockerfile_template_12x_java = '''
COPY pkg_install.sh /
RUN set -x && \\
    apt-get update -qq && \\
    apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && \\
    ./pkg_install.sh -l java -r --yes && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''


dockerfile_template_11x_all_desktop = '''
RUN set -x && \\
    apt-get -qq update && \\
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    apt-get install -y python-pip && \\
    apt-get install -y default-jre && \\
    apt-get install -y lxde xrdp && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \\
    chmod a+x pkg_install_${dist}.sh && \\
    ./pkg_install_${dist}.sh -c && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \\
    chmod a+x pkg_install_python_${dist}.sh && \\
    ./pkg_install_python_${dist}.sh -y && \\
    pip install -U pip && \\
    pip install rtshell && \\
    mkdir -p /etc/bash_completion.d/ && \\
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \\
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    ln -s /eclipse/openrtp /usr/bin/ && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y && \\
    RUN passwd -d root
'''

dockerfile_template_11x_all = '''
RUN set -x && \\
    apt-get -qq update && \\
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    apt-get install -y python-pip && \\
    apt-get install -y default-jre && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \\
    chmod a+x pkg_install_${dist}.sh && \\
    ./pkg_install_${dist}.sh -c && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \\
    chmod a+x pkg_install_python_${dist}.sh && \\
    ./pkg_install_python_${dist}.sh -y && \\
    pip install -U pip && \\
    pip install rtshell && \\
    mkdir -p /etc/bash_completion.d/ && \\
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \\
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    ln -s /eclipse/openrtp /usr/bin/ && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''

dockerfile_template_11x_cxx = '''
RUN set -x && \\
    apt-get -qq update && \\
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \\
    chmod a+x pkg_install_${dist}.sh && \\
    ./pkg_install_${dist}.sh -c && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''

dockerfile_template_11x_python = '''
RUN set -x && \\
    apt-get -qq update && \\
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    apt-get install -y python-pip && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \\
    chmod a+x pkg_install_python_${dist}.sh && \\
    ./pkg_install_python_${dist}.sh -y && \\
    apt-get autoclean -y && \\
    apt-get autoremove -y
'''

class DockerImage:
    def __init__(self, t, i, a, rv):
        self._type = t
        self._image = i
        self._dist = self._image.split(":")[0]
        self._dist_version = self._image.split(":")[1].replace(".", "")
        self._arch = a
        self._rtm_version = rv
        self._rtm_version_major = self._rtm_version.split(".")[0]
        self._rtm_version_minor = self._rtm_version.split(".")[1]
        self._rtm_version_revision = self._rtm_version.split(".")[2]

    def create(self):
        dist = self._dist + self._dist_version + self._arch
        if self._type == 'cxx':
            suffix = '-openrtm-cxx-'
        elif self._type == 'python':
            suffix = '-openrtm-python-'
        elif self._type == 'java':
            suffix = '-openrtm-java-'
        elif self._type == 'all':
            suffix = '-openrtm'
        else: # all+desktop
            suffix = '-openrtm-desktop'
        top_path = dist + suffix + self._rtm_version_major + self._rtm_version_minor + self._rtm_version_revision
        if not os.path.exists(top_path):
            os.makedirs(top_path)
        f = open(top_path + '/Dockerfile', 'w')
        print(f)

        m = dockerfile_template_common_header
        if self._rtm_version == "1.2.0":
            if self._type == 'cxx':
                m += dockerfile_template_12x_cxx
            elif self._type == 'python':
                m += dockerfile_template_12x_python
            elif self._type == 'java':
                m += dockerfile_template_12x_java
            elif self._type == 'all':
                m += dockerfile_template_12x_all
            else: # all+desktop
                m += dockerfile_template_12x_all_desktop

        else:
            if self._type == 'cxx':
                m += dockerfile_template_11x_cxx
            elif self._type == 'python':
                m += dockerfile_template_11x_python
            elif self._type == 'all':
                m += dockerfile_template_11x_all
            elif self._type == 'java':
                m += dockerfile_template_11x_all
            else: # all+desktop
                m += dockerfile_template_11x_all_desktop

        m += dockerfile_template_common_footer
        m = m.replace('@AUTHOR@', 'takahasi <3263ta@gmail.com>')
        m = m.replace('@IMAGE_NAME@', self._image)
        m = m.replace('@DISTRIBUTION@', self._dist)
        m = m.replace('@RTM_VERSION@', self._rtm_version_major + '_' + self._rtm_version_minor + '_' + self._rtm_version_revision)
        f.write(m)
        f.close()


if __name__=='__main__':

    version = [
        "1.1.2",
        "1.2.0"
    ]

    dists = [
        "ubuntu:17.04",
        "ubuntu:16.10",
        "ubuntu:16.04",
        "ubuntu:14.04",
        "ubuntu:12.04",
        # "debian:8",
        # "debian:9",
        # "fedora:24",
        # "fedora:25",
    ]

    types = [
        "all_desktop",
        "all",
        "cxx",
        "python",
        "java"
    ]

    for v in version:
        for d in dists:
            for t in types:
                DockerImage(t, d, 'x64', v).create()

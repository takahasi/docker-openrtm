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

dockerfile_template_all_desktop = '''
RUN set -x && \\
    alias apt-get='apt-get -y' && \\
    apt-get -qq update && \\
    apt-get install -y curl bc default-jre python-pip bsdmainutils apt-utils aptitude iputils-ping net-tools lxde xrdp && \\
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
    apt-get clean && \\
    apt-get autoremove && \\
    RUN passwd -d root
'''

dockerfile_template_all = '''
RUN set -x && \\
    alias apt-get='apt-get -y' && \\
    apt-get -qq update && \\
    apt-get install -y curl bc default-jre python-pip bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
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
    apt-get clean && \\
    apt-get autoremove
'''

dockerfile_template_cxx = '''
RUN set -x && \\
    alias apt-get='apt-get -y' && \\
    apt-get -qq update && \\
    apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \\
    chmod a+x pkg_install_${dist}.sh && \\
    ./pkg_install_${dist}.sh -c && \\
    apt-get clean && \\
    apt-get autoremove
'''

dockerfile_template_python = '''
RUN set -x && \\
    alias apt-get='apt-get -y' && \\
    apt-get -qq update && \\
    apt-get install -y curl bc python-pip bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_${dist}.sh && \\
    chmod a+x pkg_install_python_${dist}.sh && \\
    ./pkg_install_python_${dist}.sh -y && \\
    apt-get clean && \\
    apt-get autoremove
'''

class DockerImage:
    def __init__(self, t, d, dv, i, a, rvmj, rvmn, rvrv):
        self._dist = d
        self._dist_version = dv
        self._image = i
        self._arch = a
        self._type = t
        self._rtm_version_major = rvmj
        self._rtm_version_minor = rvmn
        self._rtm_version_revision = rvrv

    def create(self):
        dist = self._dist + self._dist_version + self._arch
        if self._type == 'cxx':
            suffix = '-openrtm-cxx-'
        elif self._type == 'python':
            suffix = '-openrtm-python-'
        elif self._type == 'all':
            suffix = '-openrtm'
        else:
            suffix = '-openrtm-desktop'
        top_path = dist + suffix + self._rtm_version_major + self._rtm_version_minor + self._rtm_version_revision
        if not os.path.exists(top_path):
            os.makedirs(top_path)
        f = open(top_path + '/Dockerfile', 'w')
        print(f)
        m = dockerfile_template_common_header
        if self._type == 'cxx':
            m += dockerfile_template_cxx
        elif self._type == 'python':
            m += dockerfile_template_python
        elif self._type == 'all':
            m += dockerfile_template_all
        else:
            m += dockerfile_template_all_desktop
        m += dockerfile_template_common_footer
        m = m.replace('@AUTHOR@', 'takahasi <3263ta@gmail.com>')
        m = m.replace('@IMAGE_NAME@', self._image)
        m = m.replace('@DISTRIBUTION@', self._dist)
        m = m.replace('@RTM_VERSION@', self._rtm_version_major + '_' + self._rtm_version_minor + '_' + self._rtm_version_revision)
        f.write(m)
        f.close()


DockerImage('all_desktop', 'ubuntu', '1704', 'ubuntu:17.04', 'x64', '1', '1', '2').create()
DockerImage('all_desktop', 'ubuntu', '1610', 'ubuntu:16.10', 'x64', '1', '1', '2').create()
DockerImage('all_desktop', 'ubuntu', '1604', 'ubuntu:16.04', 'x64', '1', '1', '2').create()
DockerImage('all_desktop', 'ubuntu', '1404', 'ubuntu:14.04', 'x64', '1', '1', '2').create()
DockerImage('all_desktop', 'ubuntu', '1204', 'ubuntu:12.04', 'x64', '1', '1', '2').create()
DockerImage('all', 'ubuntu', '1704', 'ubuntu:17.04', 'x64', '1', '1', '2').create()
DockerImage('all', 'ubuntu', '1610', 'ubuntu:16.10', 'x64', '1', '1', '2').create()
DockerImage('all', 'ubuntu', '1604', 'ubuntu:16.04', 'x64', '1', '1', '2').create()
DockerImage('all', 'ubuntu', '1404', 'ubuntu:14.04', 'x64', '1', '1', '2').create()
DockerImage('all', 'ubuntu', '1204', 'ubuntu:12.04', 'x64', '1', '1', '2').create()
DockerImage('cxx', 'ubuntu', '1704', 'ubuntu:17.04', 'x64', '1', '1', '2').create()
DockerImage('cxx', 'ubuntu', '1610', 'ubuntu:16.10', 'x64', '1', '1', '2').create()
DockerImage('cxx', 'ubuntu', '1604', 'ubuntu:16.04', 'x64', '1', '1', '2').create()
DockerImage('cxx', 'ubuntu', '1404', 'ubuntu:14.04', 'x64', '1', '1', '2').create()
DockerImage('cxx', 'ubuntu', '1204', 'ubuntu:12.04', 'x64', '1', '1', '2').create()
DockerImage('python', 'ubuntu', '1704', 'ubuntu:17.04', 'x64', '1', '1', '2').create()
DockerImage('python', 'ubuntu', '1610', 'ubuntu:16.10', 'x64', '1', '1', '2').create()
DockerImage('python', 'ubuntu', '1604', 'ubuntu:16.04', 'x64', '1', '1', '2').create()
DockerImage('python', 'ubuntu', '1404', 'ubuntu:14.04', 'x64', '1', '1', '2').create()
DockerImage('python', 'ubuntu', '1204', 'ubuntu:12.04', 'x64', '1', '1', '2').create()
#DockerImage('debian', '8', 'debian:8', 'x64', '1', '1', '2').create()
#DockerImage('debian', '9', 'debian:9', 'x64', '1', '1', '2').create()
#DockerImage('fedora', '24', 'debian:24', 'x64', '1', '1', '2').create()
#DockerImage('fedora', '25', 'fedora:25', 'x64', '1', '1', '2').create()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" script for generate dockerfile templates

This is xxx
"""

import sys
import os

dockerfile_template = '''
FROM @IMAGE_NAME@
MAINTAINER @AUTHOR@

ENV dist=@DISTRIBUTION@
ENV rtmver=@RTM_VERSION@
RUN set -x && \\
    DEBIAN_FRONTEND=noninteractive apt-get -qq update && \\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes curl bc default-jre python-pip && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_${rtmver}/OpenRTM-aist/build/pkg_install_${dist}.sh && \\
    chmod a+x pkg_install_${dist}.sh && \\
    ./pkg_install_${dist}.sh -c && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_${rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh && \\
    chmod a+x pkg_install_python_ubuntu.sh && \\
    ./pkg_install_python_ubuntu.sh -y && \\
    pip install rtshell && \\
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    cp eclipse/openrtp /usr/bin/

ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 80
'''

class DockerImage:
    def __init__(self, d, dv, i, a, rvmj, rvmn, rvrv):
        self._dist = d
        self._dist_version = dv
        self._image = i
        self._arch = a
        self._rtm_version_major = rvmj
        self._rtm_version_minor = rvmn
        self._rtm_version_revision = rvrv

    def create(self):
        dist = self._dist + self._dist_version + self._arch
        top_path = dist + '-openrtm' + self._rtm_version_major + self._rtm_version_minor + self._rtm_version_revision
        if not os.path.exists(top_path):
            os.makedirs(top_path)
        f = open(top_path + '/Dockerfile', 'w')
        print f
        m = dockerfile_template
        m = m.replace('@AUTHOR@', 'takahasi')
        m = m.replace('@IMAGE_NAME@', self._image)
        m = m.replace('@DISTRIBUTION@', self._dist)
        m = m.replace('@RTM_VERSION@', self._rtm_version_major + '_' + self._rtm_version_minor + '_' + self._rtm_version_revision)
        f.write(m)
        f.close()


DockerImage('ubuntu', '1704', 'ubuntu:17.04', 'x64', '1', '1', '2').create()
DockerImage('ubuntu', '1610', 'ubuntu:16.10', 'x64', '1', '1', '2').create()
DockerImage('ubuntu', '1604', 'ubuntu:16.04', 'x64', '1', '1', '2').create()
DockerImage('ubuntu', '1404', 'ubuntu:14.04', 'x64', '1', '1', '2').create()

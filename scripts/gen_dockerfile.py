#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" script for generate dockerfile templates

This is generating script for OpenRTM on Docker
"""

import os

dockerfile_template_common_header = '''
FROM {image}
LABEL maintainer="{maintainer}" \\
      description="OpenRTM on Docker: OpenRTM-aist on Docker images." \\
      build_type="{buildtype}"

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && apt-get update -qq
'''

dockerfile_template_common_footer = '''
RUN apt-get autoclean -y && apt-get autoremove -y

ENTRYPOINT ["/bin/bash", "-c"]
'''

dockerfile_template_12x_all_desktop = '''
COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools subversion git cmake && \\
    apt-get install -y lxde xrdp && \\
    apt-get install -y python-tk && \\
    chmod a+x ./pkg_install.sh && sync && \\
    ./pkg_install.sh -l all -c --yes && \\
    ./pkg_install.sh -l all -d --yes && \\
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \\
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \\
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make install && cd / && \\
    echo lxsession -s LXDE -e LXDE > ~/.xsession && \\
    yes root | passwd root

CMD ["/etc/init.d/xvnc", "start"]
'''

dockerfile_template_12x_all = '''
COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && sync && \\
    ./pkg_install.sh -l all -c --yes && \\
    ./pkg_install.sh -l all -d --yes && \\
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \\
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \\
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make install && cd /
'''

dockerfile_template_12x_cxx = '''
COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && sync && \\
    ./pkg_install.sh -l c++ -r --yes
'''

dockerfile_template_12x_python = '''
COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && sync && \\
    ./pkg_install.sh -l python -r --yes
'''

dockerfile_template_12x_java = '''
COPY pkg_install.sh /
RUN apt-get install -y bc iputils-ping net-tools && \\
    chmod a+x ./pkg_install.sh && sync && \\
    ./pkg_install.sh -l java -r --yes
'''


dockerfile_template_11x_all_desktop = '''
RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools subversion git cmake && \\
    apt-get install -y libopencv-dev && \\
    apt-get install -y python-pip python-tk && \\
    apt-get install -y default-jre && \\
    apt-get install -y lxde xrdp && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_{rtmver}/OpenRTM-aist/build/pkg_install_{dist}.sh && \\
    chmod a+x pkg_install_{dist}.sh && sync && \\
    ./pkg_install_{dist}.sh -c && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_{rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_{dist}.sh && \\
    chmod a+x pkg_install_python_{dist}.sh && sync && \\
    ./pkg_install_python_{dist}.sh -y && \\
    pip install -U pip && \\
    pip install rtshell && \\
    mkdir -p /etc/bash_completion.d/ && \\
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \\
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    ln -s /eclipse/openrtp /usr/bin/ && \\
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \\
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \\
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make install && cd / && \\
    echo lxsession -s LXDE -e LXDE > ~/.xsession && \\
    yes root | passwd root

CMD ["/etc/init.d/xvnc", "start"]
'''

dockerfile_template_11x_all = '''
RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    apt-get install -y python-pip && \\
    apt-get install -y default-jre && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_{rtmver}/OpenRTM-aist/build/pkg_install_{dist}.sh && \\
    chmod a+x pkg_install_{dist}.sh && sync && \\
    ./pkg_install_{dist}.sh -c && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_{rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_{dist}.sh && \\
    chmod a+x pkg_install_python_{dist}.sh && sync && \\
    ./pkg_install_python_{dist}.sh -y && \\
    pip install -U pip && \\
    pip install rtshell && \\
    mkdir -p /etc/bash_completion.d/ && \\
    cp /usr/local/lib/python2.7/dist-packages/rtshell/data/bash_completion /etc/bash_completion.d/ && \\
    curl -O http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \\
    ln -s /eclipse/openrtp /usr/bin/ && \\
    svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \\
    cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \\
    cmake -DCMAKE_INSTALL_PREFIX=/usr.. && make install && cd /
'''

dockerfile_template_11x_cxx = '''
RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_{rtmver}/OpenRTM-aist/build/pkg_install_{dist}.sh && \\
    chmod a+x pkg_install_{dist}.sh && sync && \\
    ./pkg_install_{dist}.sh -c
'''

dockerfile_template_11x_python = '''
RUN apt-get install -y curl bc bsdmainutils apt-utils aptitude iputils-ping net-tools && \\
    apt-get install -y python-pip && \\
    curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_{rtmver}/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_{dist}.sh && \\
    chmod a+x pkg_install_python_{dist}.sh && sync && \\
    ./pkg_install_python_{dist}.sh -y
'''


class DockerImage:
    def __init__(self, t, i, a, rv):
        self._type = t
        self._image = i
        self._dist = i.split(":")[0]
        self._rtm_ver_major = rv.split(".")[0]
        self._rtm_ver_minor = rv.split(".")[1]
        self._rtm_ver_rev = rv.split(".")[2]

        dist_ver = i.split(":")[1].replace(".", "")
        arch = a

        dist = self._dist + dist_ver + arch
        if self._type == 'cxx':
            suffix = '-openrtm-cxx-'
        elif self._type == 'python':
            suffix = '-openrtm-python-'
        elif self._type == 'java':
            suffix = '-openrtm-java-'
        elif self._type == 'all':
            suffix = '-openrtm'
        else:  # all+desktop
            suffix = '-openrtm-desktop'
        self._top_path = dist + suffix + self._rtm_ver_major + self._rtm_ver_minor + self._rtm_ver_rev

    def dockerfile_11x(self):
        m = dockerfile_template_common_header
        if self._type == 'cxx':
            m += dockerfile_template_11x_cxx
        elif self._type == 'python':
            m += dockerfile_template_11x_python
        elif self._type == 'java':
            m += dockerfile_template_11x_all
        elif self._type == 'all':
            m += dockerfile_template_11x_all
        else:  # all+desktop
            m += dockerfile_template_11x_all_desktop

        m += dockerfile_template_common_footer
        return m

    def dockerfile_12x(self):
        m = dockerfile_template_common_header
        if self._type == 'cxx':
            m += dockerfile_template_12x_cxx
        elif self._type == 'python':
            m += dockerfile_template_12x_python
        elif self._type == 'java':
            m += dockerfile_template_12x_java
        elif self._type == 'all':
            m += dockerfile_template_12x_all
        else:  # all+desktop
            m += dockerfile_template_12x_all_desktop

        m += dockerfile_template_common_footer
        return m

    def create(self):
        if not os.path.exists(self._top_path):
            os.makedirs(self._top_path)

        f = open(self._top_path + '/Dockerfile', 'w')
        print(f)

        if self._rtm_ver_major == "1":
            m = ""
            if self._rtm_ver_minor == "2":
                m = self.dockerfile_12x()
            elif self._rtm_ver_minor == "1":
                m = self.dockerfile_11x()
            else:
                print("Unknown version!!")
                return

            m = m.format(maintainer="takahasi <3263ta@gmail.com>",
                         image=self._image,
                         dist=self._dist,
                         buildtype=self._dist + '-' + self._type,
                         rtmver=self._rtm_ver_major + '_' + self._rtm_ver_minor + '_' + self._rtm_ver_rev)
            f.write(m)
        else:
            print("Unknown version!!")

        f.close()


if __name__ == '__main__':

    version = [
        "1.1.2",
        "1.2.0"
    ]

    dists = [
        "ubuntu:17.10",
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

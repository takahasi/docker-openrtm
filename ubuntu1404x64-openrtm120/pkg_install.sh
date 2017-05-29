#!/bin/sh
#
# @file pkg_install_ubuntu.sh
# @brief OpenRTM-aist dependent packages install script for Ubuntu
# @author Noriaki Ando <n-ando@aist.go.jp>
#         Shinji Kurihara
#         Tetsuo Ando
#         Harumi Miyamoto
#         Seisho Irie
#         Nobu   Kawauchi
#

#---------------------------------------
# usage
#---------------------------------------
usage()
{
  cat <<EOF
  Usage: 

    $(basename ${0}) [-l all/c++] [-r/-d/-s/-c] [-u]
    $(basename ${0}) [-l python/java] [-d/-c] [-u]
    $(basename ${0}) [-l openrtp/rtshell] [-d] [-u]                           

  Example:
    $(basename ${0})  [= $(basename ${0}) -l c++ -d]
    $(basename ${0}) -l all -d  [= -l c++ -l python -l java -l openrtp -l rtshell -d]
    $(basename ${0}) -l c++ -l python -c --yes

  Options:
    -l <argument>  language or tool [c++/python/java/openrtp/rtshell]
    -r             install robot component runtime
    -d             install robot component developer [default]
    -s             install tool_packages for build source packages
    -c             install tool_packages for core developer
    -u             uninstall
    --yes          force yes
    --help, -h     print this
EOF
}

#---------------------------------------
# パッケージリスト
#---------------------------------------
ace="libace libace-dev"
openrtm04="openrtm-aist=0.4.2-1 openrtm-aist-doc=0.4.2-1 openrtm-aist-dev=0.4.2-1 openrtm-aist-example=0.4.2-1 python-yaml"

#default_reposerver="openrtm.org"
#reposervers="openrtm.org"
default_reposerver="staging.openrtm.org"
reposervers="staging.openrtm.org"
reposerver=""

#--------------------------------------- C++
autotools="autoconf libtool libtool-bin"
cxx_devel="gcc g++ make python-yaml"
cmake_tools="cmake doxygen"
build_tools="subversion"
deb_pkg="uuid-dev libboost-filesystem-dev"
pkg_tools="build-essential debhelper devscripts"
omni_devel="libomniorb4-dev omniidl"
omni_runtime="omniorb-nameserver"
openrtm_devel="openrtm-aist-doc openrtm-aist-dev"
openrtm_runtime="openrtm-aist openrtm-aist-example"

runtime_pkgs="$omni_runtime $openrtm_runtime"
u_runtime_pkgs=$runtime_pkgs

src_pkgs="$cxx_devel $cmake_tools $deb_pkg $omni_runtime $omni_devel"
u_src_pkgs="$omni_runtime $omni_devel"

dev_pkgs="$runtime_pkgs $src_pkgs $openrtm_devel"
u_dev_pkgs="$u_runtime_pkgs $u_src_pkgs $openrtm_devel"

core_pkgs="$src_pkgs $autotools $build_tools $pkg_tools"
u_core_pkgs="$u_src_pkgs"

#--------------------------------------- Python
omnipy="omniidl-python"
python_devel="python python-pip python-pyorbit-omg"
openrtm_py_devel="openrtm-aist-python-doc"
openrtm_py_runtime="openrtm-aist-python openrtm-aist-python-example"

python_base="$python_devel $cmake_tools"
python_omni="$omni_runtime $omnipy"

python_dev_pkgs="$python_base $python_omni $openrtm_py_devel $openrtm_py_runtime"
u_python_dev_pkgs="$python_omni $openrtm_py_devel $openrtm_py_runtime"

python_core_pkgs="$python_base $python_omni $build_tools"
u_python_core_pkgs="$python_omni"

#--------------------------------------- Java
java_devel="default-jdk"
openrtm_java_devel="openrtm-aist-java-doc"
openrtm_java_runtime="openrtm-aist-java openrtm-aist-java-example"

java_dev_pkgs="$java_devel $cmake_tools $openrtm_java_devel $openrtm_java_runtime"
u_java_dev_pkgs="$openrtm_java_devel $openrtm_java_runtime"

java_core_pkgs="$java_devel $cmake_tools $build_tools"
u_java_core_pkgs=

#--------------------------------------- OpenRTP
openrtp_pkgs="openrtp"

#---------------------------------------
# Script options, argument analysis
#---------------------------------------
init_param()
{
OPT_RT=false
OPT_DEV=false
OPT_SRC=false
OPT_CORE=false
OPT_FLG=true
}

check_arg()
{
  local arg=$1
  arg_err=0
  
  case "$arg" in
    all ) arg_all=true ;;
    c++ ) arg_cxx=true ;;
    python ) arg_python=true ;;
    java ) arg_java=true ;;
    openrtp ) arg_openrtp=true ;;
    rtshell ) arg_rtshell=true ;;
    *) arg_err=-1 ;;
  esac
}

get_opt()
{ 
  # オプション指定が無い場合のデフォルト設定
  if [ $# -eq 0 ] ; then
    arg_cxx=true
    OPT_DEV=true
  fi
  arg_num=$#
 
  OPT=`getopt -o l:rcsdhu -l help,yes -- $@` > /dev/null 2>&1
  # return code check
  if [ $? -ne 0 ] ; then
    echo "[ERROR] Invalid option '$1'"
    usage
    exit
  fi
  eval set -- $OPT

  while true
  do
    case "$1" in
        -h|--help ) usage ; exit ;;
        --yes ) FORCE_YES=true ;;
        -l )  if [ -z "$2" ] ; then
                echo "$1 option requires an argument." 1>&2
                exit
              fi
              check_arg $2
              if [ "$arg_err" = "-1" ]; then
                echo "[ERROR] Invalid argument '$2'"
                usage
                exit
              fi
              shift ;;
        -r )  OPT_RT=true ;;
        -d )  OPT_DEV=true ;;
        -s )  OPT_SRC=true ;;
        -c )  OPT_CORE=true ;;
        -u )  OPT_FLG=false ;;
        -- ) shift ; break ;;                 
        * )
          echo "Internal Error" 1>&2
          exit ;;
    esac
    shift
  done

  # オプション指定が -u のみの場合
  if [ $arg_num -eq 1 ] ; then
    if test "x$OPT_FLG" = "xfalse" ; then 
      arg_cxx=true
    fi
  fi
}

#---------------------------------------
# ロケールの言語確認
#---------------------------------------
check_lang()
{
lang="en"

locale | grep ja_JP > /dev/null && lang="jp"

if test "$lang" = "jp" ;then
    msg1="ディストリビューションを確認してください。\nDebianかUbuntu以外のOSの可能性があります。"
    msg2="コードネーム :"
    msg3="このOSはサポートしておりません。"
    msg4="OpenRTM-aist のリポジトリが登録されていません。"
    msg5="Source.list に OpenRTM-aist のリポジトリ: "
    msg6="を追加します。よろしいですか？(y/n)[y] "
    msg7="中断します。"
    msg8="ルートユーザーで実行してください。"
    msg9="インストール中です..."
    msg10="完了"
    msg11="アンインストール中です."
else
    msg1="This distribution may not be debian/ubuntu."
    msg2="The code name is : "
    msg3="This OS is not supported."
    msg4="No repository entry for OpenRTM-aist is configured in your system."
    msg5="repository entry for OpenRTM-aist: "
    msg6="Do you want to add new repository entry for OpenRTM-aist in source.list? (y/n) [y] "
    msg7="Abort."
    msg8="This script should be run as root."
    msg9="Now installing: "
    msg10="done."
    msg11="Now uninstalling: "
fi

}

#----------------------------------------
# 近いリポジトリサーバを探す
#----------------------------------------
check_reposerver()
{
  minrtt=65535
  nearhost=''
  for host in $reposervers; do
    rtt=`ping -c 1 $host | grep 'time=' | sed -e 's/^.*time=\([0-9\.]*\) ms.*/\1/' 2> /dev/null`
    if test "x$rtt" = "x"; then
      rtt=65535
    fi
    if test `echo "scale=2 ; $rtt < $minrtt" | bc` -gt 0; then
      minrtt=$rtt
      nearhost=$host
    fi
  done
  if test "x$nearhost" = "x"; then
    echo "Repository servers unreachable.", $hosts
    echo "Check your internet connection. (or are you using proxy?)"
    nearhost=$default_reposerver
  fi
  reposerver=$nearhost
}

#---------------------------------------
# リポジトリサーバ
#---------------------------------------
create_srclist () {
  codename=`sed -n /DISTRIB_CODENAME=/p /etc/lsb-release`
  cnames=`echo "$codename" | sed 's/DISTRIB_CODENAME=//'`
  for c in $cnames; do
    if test -f "/etc/apt/sources.list"; then
      res=`grep $c /etc/apt/sources.list`
    else
      echo $msg1
      exit
    fi
    if test ! "x$res" = "x" ; then
      code_name=$c
    fi
  done
  if test ! "x$code_name" = "x"; then
    echo $msg2 $code_name
  else
    echo $msg3
    exit
  fi
  openrtm_repo="deb http://$reposerver/pub/Linux/ubuntu/ $code_name main"
}

#---------------------------------------
# ソースリスト更新関数の定義
#---------------------------------------
update_source_list () {
  rtmsite=`grep "$openrtm_repo" /etc/apt/sources.list`
  if test "x$rtmsite" = "x" ; then
    echo $msg4
    echo $msg5
    echo "  " $openrtm_repo
    read -p "$msg6" kick_shell

    if test "x$kick_shell" = "xn" ; then
      echo $msg7
      exit 0
    else
      echo $openrtm_repo >> /etc/apt/sources.list
      apt-key adv --keyserver keys.gnupg.net --recv-keys 4BCE106E087AFAC0
    fi
  fi
}

#----------------------------------------
# root かどうかをチェック
#----------------------------------------
check_root () {
  if test ! `id -u` = 0 ; then
    echo ""
    echo $msg8
    echo $msg7
    echo ""
    exit 1
  fi
}

#----------------------------------------
# パッケージインストール関数
#----------------------------------------
install_packages () {
  for p in $*; do
    echo $msg9 $p
    if test "x$FORCE_YES" = "xtrue" ; then
      apt-get install --assume-yes --allow-unauthenticated $p
    else
      apt-get install $p
    fi
    echo $msg10
    echo ""
  done
}

#------------------------------------------------------------
# リストを逆順にする
#------------------------------------------------------------
reverse () {
  for i in $*; do
    echo $i
  done | sed '1!G;h;$!d'
}

#----------------------------------------
# パッケージをアンインストールする
#----------------------------------------
uninstall_packages () {
  for p in $*; do
    echo $msg11 $p
    apt-get remove $p
    if test "$?" != 0; then
      apt-get purge $p
    fi
    echo $msg10
    echo ""
  done
}

#---------------------------------------
# install_branch
#---------------------------------------
install_branch()
{
  if test "x$arg_cxx" = "xtrue" ; then
    if test "x$OPT_CORE" = "xtrue" ; then
      echo "[c++] install tool_packages for core developer"
      install_packages $core_pkgs
    elif test "x$OPT_SRC" = "xtrue" ; then
      echo "[c++] install tool_packages for source packages"
      install_packages $src_pkgs
    elif test "x$OPT_RT" = "xtrue" ; then
      echo "[c++] install robot component runtime"
      install_packages $runtime_pkgs
    else
      echo "[c++] install robot component developer"
      install_packages $dev_pkgs
    fi
  fi

  if test "x$arg_python" = "xtrue" ; then
    if test "x$OPT_CORE" = "xtrue" ; then
      echo "[python] install tool_packages for core developer"
      install_packages $python_core_pkgs
    else
      echo "[python] install robot component developer"
      install_packages $python_dev_pkgs
    fi
  fi

  if test "x$arg_java" = "xtrue" ; then
    if test "x$OPT_CORE" = "xtrue" ; then
      echo "[java] install tool_packages for core developer"
      install_packages $java_core_pkgs
    else
      echo "[java] install robot component developer"
      install_packages $java_dev_pkgs
    fi
  fi

  if test "x$arg_openrtp" = "xtrue" ; then
    echo "[openrtp] install"
    install_packages $openrtp_pkgs
  fi

  if test "x$arg_rtshell" = "xtrue" ; then
    echo "[rtshell] install"
    pip install rtshell
  fi
  exit
}

#---------------------------------------
# uninstall_branch
#---------------------------------------
uninstall_branch()
{
  if test "x$arg_cxx" = "xtrue" ; then
    if test "x$OPT_CORE" = "xtrue" ; then
      echo "[c++] uninstall tool_packages for core developer"
      uninstall_packages `reverse $u_core_pkgs`
    elif test "x$OPT_SRC" = "xtrue" ; then
      echo "[c++] uninstall tool_packages for source packages"
      uninstall_packages `reverse $u_src_pkgs`
    elif test "x$OPT_RT" = "xtrue" ; then
      echo "[c++] uninstall robot component runtime"
      uninstall_packages `reverse $u_runtime_pkgs`
    else
      echo "[c++] uninstall robot component developer"
      uninstall_packages `reverse $u_dev_pkgs`
    fi
  fi

  if test "x$arg_python" = "xtrue" ; then
    if test "x$OPT_CORE" = "xtrue" ; then
      echo "[python] uninstall tool_packages for core developer"
      uninstall_packages `reverse $u_python_core_pkgs`
    else
      echo "[python] uninstall robot component developer"
      uninstall_packages `reverse $u_python_dev_pkgs`
    fi
  fi

  if test "x$arg_java" = "xtrue" ; then
    if test "x$OPT_CORE" = "xtrue" ; then
      echo "[java] uninstall tool_packages for core developer"
      uninstall_packages `reverse $u_java_core_pkgs`
    else
      echo "[java] uninstall robot component developer"
      uninstall_packages `reverse $u_java_dev_pkgs`
    fi
  fi

  if test "x$arg_openrtp" = "xtrue" ; then
    echo "[openrtp] uninstall"
    uninstall_packages $openrtp_pkgs
  fi

  if test "x$arg_rtshell" = "xtrue" ; then
    echo "[rtshell] uninstall"
    pip uninstall -y rtshell
  fi
  exit
}

#---------------------------------------
# メイン
#---------------------------------------
init_param
get_opt $@

check_lang
check_root
check_reposerver
create_srclist
update_source_list
apt-get autoclean
apt-get update

if test "x$arg_all" = "xtrue" ; then
  arg_cxx=true
  arg_python=true
  arg_java=true
  arg_openrtp=true
  arg_rtshell=true
  if test "x$OPT_FLG" = "xtrue" ; then
    if test "x$OPT_DEV" != "xtrue" ; then
      OPT_CORE=true
    fi
    install_branch
  else
    uninstall_branch
  fi
fi

if test "x$OPT_FLG" = "xtrue" ; then
  install_branch
else
  uninstall_branch
fi


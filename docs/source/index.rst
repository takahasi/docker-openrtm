.. test documentation master file, created by
   sphinx-quickstart on Mon Nov 28 17:18:29 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

openRTM on Docker
=================

.. list-table::

  * - Version
    - |release|
  * - Last Update
    - |today|
  * - Author
    - Saburo Takahashi

更新履歴
========

.. csv-table::
  :header-rows: 1
  :widths: 1, 3, 2, 8, 4
  :file: ../data/history.csv


目次
====

.. toctree::
   :maxdepth: 2
   :numbered:
   :glob:

   index

0. OpenRTM on Dockerって何？
============================
OpenRTM on Dockerは `OpenRTM-aist <http://www.openrtm.org/openrtm/>`_ がインストールされたDockerイメージおよび周辺ツール群の総称です．

開発の動機
----------
OpenRTM-aistをもっと簡単に使いたい！
````````````````````````````````````
RTコンポーネント(RTC)を開発する場合、汎用性や後方互換製に配慮する必要があります．
そのためには、OSのバージョンやRTミドルウェアのバージョン、開発PCにインストールされているさまざまなライブラリとの依存関係を疎にする必要があります．
この作業、特に開発環境を整備することが非常に大変で、開発コストの増加に繋がります．
そこで、RTミドルウェアを含むさまざまなライブラリの組み合わせをDockerイメージとして提供することで、開発環境構築コストを低減できると考えました．
また，RTミドルウェア講習会などを通じて，OpenRTM-aistインストールにおけるトラブル事例が多く発生しており，その原因が各自のホスト環境の違いに起因していると感じていました．
OpenRTM on Docker はホストOSの環境差異を吸収でき，実行環境に依らず不変（immutable）な動作ができます．


1. 概要
=======

1.1. 目的
---------

本書はOpenRTM on Dockerの機能や利用方法について記載したドキュメントです．



1.2. 位置づけ
-------------

本書はOpenRTM on Dockerを利用しているユーザ，および利用を検討している方に向けたドキュメントです．

1.3. 対象ユーザ
------------------

* RTC設計，開発，検証担当者
* RTシステム検証担当者
* RTCおよびRTシステムリリース，運用担当者
* RTM設計，開発，検証担当者
* RTMリリース，運用担当者
* RTM講習会，チュートリアル受講生

1.4. 記載範囲
------------------

* 概要
* 機能
* 制約条件
* 使用方法
* FAQ

1.5. 参照ドキュメント/URL
-------------------------

.. csv-table:: 参照ドキュメント/URL一覧
  :header-rows: 1
  :widths: 1, 4, 6
  :file: ../data/references.csv


1.6. 定義（用語、略語）
-----------------------

.. csv-table:: 用語定義一覧
  :header-rows: 1
  :widths: 1, 4, 6
  :file: ../data/grossary.csv


2. システム構成
==================

OpenRTM on Dockerに含まれるDockerイメージははDocker Engine上で動作するOSとOpenRTM-aistをまとめたコンテナです．

.. image:: ../img/basic.png
  :width: 50%
  :align: center


3. 機能概要
==================

OpenRTM on Dockerができること
-----------------------------
- OpenRTM-aist をインストールせずに利用することができる
 - OpenRTPやサンプルコンポーネントをホストPCにインストールせずに起動できる
- 様々なバージョンのOpenRTM-aistを利用したコンパイルや動作確認ができる
 - OS（Ubuntu/Debian/Fedora），OpenRTM-aist（1.1.2/1.2.0（開発途中版）），言語（C++，Python，Java）などの組み合わせが準備済み 
- OpenRTM on Docker を簡単に試すことができるスクリプト群を整備

.. list-table:: OpenRTM on Dockerの応用イメージ

  * - .. image:: ../img/sample1.png
        :width: 100%
    - .. image:: ../img/sample2.png
        :width: 100%


4. 制約条件
==================


ライセンス
-----------------------------
OpenRTM on Docker に含まれる Dockerfile やツール群はMITライセンスにより配布されます．
しかし，OpenRTM on Docker イメージに含まれるOSおよび周辺ソフトウェア，OpenRTM-aistのライセンスは別です．
また，ホストOSにインストールされた Docker エンジンについてもライセンスは別扱いとなります．
利用時は最新の情報やインストールしたバージョンを確認し，ライセンス条約に遵守するようにして下さい．

下記に関連する代表的なソフトウェアのライセンス記載箇所を示しますが，
これらは本書執筆時点の情報であるため，
再配布等を行う場合は利用者が再度確認してご利用下さい．

.. list-table:: 代表的なソフトウェアの欄センス

  * - Docker Community Edition
    - Apache License 2.0
    - https://github.com/moby/moby/blob/master/LICENSE
  * - Docker Components
    - 右記参照
    - https://www.docker.com/components-licenses
  * - OpenRTM-aist
    - | OpenRTM-aist (C++、Java、Python版)は LGPL と個別契約のデュアルライセンス
      | RTSystemEditor、RTCBuilder は EPL と個別契約のデュアルライセンス
    - http://openrtm.org/openrtm/ja/content/openrtm-aist%E3%81%A8%E3%81%AF%EF%BC%9F-0
  * - OpenRTM on Docker
    - MIT License
    - https://github.com/takahasi/docker-openrtm/blob/master/LICENSE


Apache License 2.0


5. 使用方法
==================
インストールする必要があるのは Docker とその依存パッケージのみです．
OpenRTM-aist に関係するパッケージのインストールは一切必要ありません．

現在 OpenRTM on Docker の動作が確認できているのは下記のホストOSです．
下記はDockerが正式サポートしているものを列挙していますが，
下記以外においても Docker がインストールできれば動作可能です．

.. list-table:: 動作確認できているOS
  :header-rows: 0
  :stub-columns: 1

  * - Windows
    - | Windows Server 2016 64bit（確認中）
      | Windows 10 64bit
  * - Linux
    - | Ubuntu 14.04 64bit
      | Ubuntu 16.04 64bit
      | Ubuntu 17.04 64bit
      | Ubuntu 17.10 64bit（確認中）
      | Fedora 24（確認中）
      | Fedora 25（確認中）
      | CentOS 7（確認中）
      | Debian Wheezy 7.7
      | Debian Jessie 8
      | Debian Stretch 9（確認中）
      | Debian Buster 10（確認中）
      | Raspbian
  * - Mac
    - | OS X El Capitan 10.11
      | macOS Sierra 10.12（確認中）
      | macOS High Sierra 10.13（確認中）


Dockerのインストール
--------------------
最新のインストール方法はDockerホームページに記載されています．
https://docs.docker.com/engine/installation/

現在，DockerにはCommunication EditionとEnterprise Editionの2種があります．
本書では無料で利用可能な Communication Edition を使用する想定で記載していますが，
Enterprise Editionを利用する場合でも一部インストール中の画面構成等が異なるだけで，
本書記載のOpenRTM on Dockerの機能は利用できます．

* Windows の場合: 

.. code-block:: sh

  wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-install.bat
  chmod +x docker-install.sh
  ./docker-install.sh

- Linux(Ubuntu)の場合: 

.. code-block:: sh

  wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-install.sh
  chmod +x docker-install.sh
  ./docker-install.sh

* Linux(Debian)の場合

* Linux(Fedora)の場合


* MacOSX の場合

* FreeBSDの場合


OpenRTM on Docker 使用方法
--------------------------
Docker がインストールされている環境であれば OpenRTM on Docker が利用できます．  
イメージをダウンロードしてキャッシュするため，初回起動時は外部ネットワークに接続されている必要があり，  
初回起動時のみ起動まで時間がかかります（ネットワーク環境に依存しますが，数分程度）．  
一度キャッシュされてしまえば，２回目移行の起動は速くなります（コンピュータスペックに依存しますが１秒未満）．

おすすめの利用方法(Linux ホストの場合) 
``````````````````````````````````````
- 最新の全パッケージ入り OpenRTM on Docker イメージを利用します
- HOMEディレクトリが共有されてDockerイメージ内のシェルが起動します  
- シェルを抜けるとコンテナが消去されます: 

.. code-block:: sh

  wget https://raw.githubusercontent.com/takahasi/docker-openrtm-tools/master/tools/rtmdocker.sh
  chmod +x rtｍdocker.sh
  ./rtmdocker.sh

Docker コマンドで直接イメージを起動: 
``````````````````````````````````````

.. code-block:: sh

  docker run --rm -ti takahasi/docker-openrtm bash

イメージのバージョンを指定し起動する方法: 
```````````````````````````````````````````

.. code-block:: sh

  docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash

Dockerfileを使ってOpenRTM on Dockerイメージをカスタマイズする方法
```````````````````````````````````````````````````````````````````

下記を Dockerfile に記載することで，ベースとなるOpenRTM on  Docker イメージを利用できます．: 

.. code-block:: sh

  FROM takahasi/docker-openrtm:ubuntu1404_openrtm112


例えば，自作したコンポーネントを起動時に動作させるためには，
下記のような Dockerfile を作成することでカスタムイメージを作成できます．: 

.. code-block:: sh

  FROM takahasi/docker-openrtm:ubuntu1404_openrtm112
  
  COPY MyComponent /usr/local/bin/
  CMD ["MyComponent", ""]



GUIアプリケーションを使う方法
````````````````````````````````````````````````````````

リモートデスクトッププロトコル(RDP)で接続する場合
''''''''''''''''''''''''''''''''''''''''''''''''''''

RDP（Remote Desktop Protocol）サーバがインストールされたイメージを利用している場合，
リモートデスクトップクライアントをホストにインストールし，
リモートデスクトップクライアントからローカルホストに対して接続することで，
OpenRTM on Dockerコンテナ内のデスクトップ画面を表示することができます．

* ユーザ名:root
* パスワード:root


Xウィンドウを利用して接続する場合  (Linux/Mac ホストの場合) :  
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: sh

  wget https://raw.githubusercontent.com/takahasi/docker-openrtm-tools/master/tools/rtmdocker.sh
  chmod +x ｒｔｍdocker.sh
  ./rtmdocker.sh


6. 利用できるイメージ
=====================

.. csv-table:: 利用できるイメージ一覧
  :header-rows: 1
  :widths: 6, 4, 3, 2, 2, 2, 2, 2, 3
  :file: ../data/images.csv

7. FAQ
=====================

* 利用可能なPCのスペックは？
* 動作性能は？
* 利用ライセンスは？
* 必要なスキルは？
* バグを発見した場合には？


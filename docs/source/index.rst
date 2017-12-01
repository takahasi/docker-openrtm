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
OpenRTM on Dockerは[OpenRTM-aist](http://www.openrtm.org/openrtm/)がインストールされたDockerイメージおよび周辺ツール群の総称です。

開発の動機
----------
OpenRTM-aistをもっと簡単に使いたい！
````````````````````````````````````
RTコンポーネント(RTC)を開発する場合、汎用性や後方互換製に配慮する必要があります。  
そのためには、OSのバージョンやRTミドルウェアのバージョン、開発PCにインストールされているさまざまなライブラリとの依存関係を疎にする必要があります。
この作業、特に開発環境を整備することが非常に大変で、開発コストの増加に繋がります。  
そこで、RTミドルウェアを含むさまざまなライブラリの組み合わせをDockerイメージとして提供することで、開発環境構築コストを低減できると考えました。  

1. 概要
=======

1.1. 目的
---------

本書はxxx


1.2. 位置づけ
-------------

本書はxxx

1.3. 対象ユーザ
------------------

* システム発注者およびその関係者
* システムアーキテクチャ設計者
* システム安全要求分析者
* システムテスト設計者
* ソフトウェア要求分析者


1.4. 記載範囲
------------------

* システム概要
* システム構成
* 機能概要
* 制約条件
* ユースケース
* 機能詳細
* 非機能要求詳細

1.5. 参照ドキュメント/URL
-------------------------

.. csv-table:: 参照ドキュメント/URL一覧
  :header-rows: 1
  :widths: 1, 4, 6
  :file: ../data/references.csv


1.6. 定義（用語、略語）
-----------------------



2. システム構成
==================

OpenRTM on Dockerに含まれるDockerイメージははDocker Engine上で動作するOSとOpenRTM-aistをまとめたコンテナです．

.. image:: ../img/basic.png



3. 機能概要
==================

OpenRTM on Dockerができること
----------------------------
- OpenRTM-aist をインストールせずに利用することができる
 - OpenRTPやサンプルコンポーネントをホストPCにインストールせずに起動できる
- 様々なバージョンのOpenRTM-aistを利用したコンパイルや動作確認ができる
 - OS（Ubuntu/Debian/Fedora），OpenRTM-aist（1.1.2/1.2.0（開発途中版）），言語（C++，Python，Java）などの組み合わせが準備済み 
- OpenRTM on Docker を簡単に試すことができるスクリプト群を整備




4. 制約条件
==================



5. 使用方法
==================
インストールする必要があるのは Docker とその依存パッケージのみです．

OpenRTM-aist に関係するパッケージのインストールは一切必要ありません．

現在 OpenRTM on Docker の動作が確認できているのは下記のホストOSです．


.. list-table:: 動作確認できているOS
  :header-rows: 0
  :stub-columns: 1

  * - Windows
    - Windows 10 64bit
  * - Linux
    - Ubuntu 14.04 64bit
      Ubuntu 16.04 64bit
      Fedora
      Debian
      Raspbian
  * - Mac OSX
    - 10.11 El Capitan
  * - FreeBSD
    - x

Dockerのインストール
--------------------
最新の情報はDockerホームページに記載されています．
https://docs.docker.com/engine/installation/

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

簡単に試す方法: 
``````````````````````````````````````

.. code-block:: sh

  docker run --rm -ti takahasi/docker-openrtm bash

バージョンを指定して実行する方法: 
``````````````````````````````````````

.. code-block:: sh

  docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash

Dockerfileを使って、イメージをカスタマイズする方法: 
````````````````````````````````````````````````````````

.. code-block:: sh

  FROM takahasi/docker-openrtm:ubuntu1404_openrtm112

![OpenRTM on Docker as a Development Environment](../img/sample1.png)

![OpenRTM on Docker as a Verification Environment](../img/sample2.png)

GUIアプリケーションを使う方法
````````````````````````````````````````````````````````

リモートデスクトッププロトコル(RDP)で接続する場合
''''''''''''''''''''''''''''''''''''''''''''''''''''
(default user:root, password:root)  


Xウィンドウを利用して接続する場合  (Linux/Mac ホストの場合) :  
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: sh

  wget https://raw.githubusercontent.com/takahasi/docker-openrtm-tools/master/tools/rtmdocker.sh
  chmod +x ｒｔｍdocker.sh
  ./rtmdocker.sh


6. 利用できるイメージ
=====================

.. csv-table::
  :header-rows: 1
  :widths: 6, 4, 2, 2, 2, 2, 2, 2, 3
  :file: ../data/images.csv

7. FAQ
=====================

* 利用可能なPCのスペックは？
* 動作性能は？
* 利用ライセンスは？
* 必要なスキルは？
* バグを発見した場合には？


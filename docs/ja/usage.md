[English](../usage)


インストール方法
================
インストールする必要があるのは Docker とその依存パッケージのみです．  
OpenRTM-aist に関係するパッケージのインストールは一切必要ありません．

- Windows(64bit版のみ)
  - 10
- Linux(64bit版のみ)
  - Ubuntu
  - Fedora
  - Debian
  - Raspbian
- MacOSX
  - El Capitan 10.11 以降
- FeeBSD

Dockerのインストール
--------------------
最新の情報はDockerホームページに記載されています．
https://docs.docker.com/engine/installation/

- Windows の場合

`wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-install.bat`  
`chmod +x docker-install.sh`  
`./docker-install.sh`

- Linux(Ubuntu)の場合

`wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-install.sh`  
`chmod +x docker-install.sh`  
`./docker-install.sh`

- Linux(Debian)の場合

- Linux(Fedora)の場合


- MacOSX の場合

- FreeBSDの場合


OpenRTM on Docker 使用方法
===========================
Docker がインストールされている環境であれば OpenRTM on Docker が利用できます．  
イメージをダウンロードしてキャッシュするため，初回起動時は外部ネットワークに接続されている必要があり，  
初回起動時のみ起動まで時間がかかります（ネットワーク環境に依存しますが，数分程度）．  
一度キャッシュされてしまえば，２回目移行の起動は速くなります（コンピュータスペックに依存しますが１秒未満）．

おすすめの利用方法(Linux ホストでの利用) 
---------------------------------------- 
* 最新の全パッケージ入り OpenRTM on Docker イメージを利用します
* HOMEディレクトリが共有されてDockerイメージが起動します  
* シェルを抜けるとコンテナが消去されます  
`wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-run.sh`  
`chmod +x docker-run.sh`  
`./docker-run.sh`

簡単に試す方法
---------------
`docker run --rm -ti takahasi/docker-openrtm bash`

バージョンを指定して実行する方法
---------------------------------
`docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash`

Dockerfileを使って、イメージをカスタマイズする方法
---------------------------------------------------
`FROM takahasi/docker-openrtm:ubuntu1404_openrtm112`

![OpenRTM on Docker as a Development Environment](../img/sample1.png)

![OpenRTM on Docker as a Verification Environment](../img/sample2.png)

GUIアプリケーションを使う場合
-----------------------------

### RDP
リモートデスクトッププロトコル(RDP)で接続する場合(Desktopのみ)  
(default user:root, password:root)  

### X-forwarding
Xウィンドウを利用して接続する場合  
(Linux host only)  

`wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-run.sh`  
`chmod +x docker-run.sh`  
`./script/docker-run.sh`


[Top Page](index)

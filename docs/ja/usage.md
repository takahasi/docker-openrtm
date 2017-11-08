[English](../usage)

使用方法
========
おすすめの方法(Linux ホストのみ)  
* HOMEディレクトリが共有されてDockerイメージが起動します  
* シェルを抜けるとコンテナが消去されます  
`wget https://raw.githubusercontent.com/takahasi/docker-openrtm/master/scripts/docker-run.sh`  
`chmod +x docker-run.sh`  
`./docker-run.sh`

簡単に試す方法。  
`docker run --rm -ti takahasi/docker-openrtm bash`

バージョンを指定して実行する方法。  
`docker run --rm -ti takahasi/docker-openrtm:ubuntu1404_openrtm112 bash`

Dockerfileを使って、イメージをカスタマイズする方法。  
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

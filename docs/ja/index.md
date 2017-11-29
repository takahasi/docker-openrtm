[English](../index)

OpenRTM on Docker (docker-openrtm)
==================================

---

**OpenRTM on Docker**って何？
---------------------------
**OpenRTM on Docker**は[OpenRTM-aist](http://www.openrtm.org/openrtm/)がインストールされたDockerイメージおよび周辺ツール群の総称です。

---

開発の動機
--------
### OpenRTM-aistをもっと簡単に使いたい！
RTコンポーネント(RTC)を開発する場合、汎用性や後方互換製に配慮する必要があります。  
そのためには、OSのバージョンやRTミドルウェアのバージョン、開発PCにインストールされているさまざまなライブラリとの依存関係を疎にする必要があります。
この作業、特に開発環境を整備することが非常に大変で、開発コストの増加に繋がります。  
そこで、RTミドルウェアを含むさまざまなライブラリの組み合わせをDockerイメージとして提供することで、開発環境構築コストを低減できると考えました。  

---

OpenRTM on Dockerができること
----------------------------
- OpenRTM-aist をインストールせずに利用することができる
 - OpenRTPやサンプルコンポーネントをホストPCにインストールせずに起動できる
- 様々なバージョンのOpenRTM-aistを利用したコンパイルや動作確認ができる
 - OS（Ubuntu/Debian/Fedora），OpenRTM-aist（1.1.2/1.2.0（開発途中版）），言語（C++，Python，Java）などの組み合わせが準備済み 
- OpenRTM on Docker を簡単に試すことができるスクリプト群を整備

---

OpenRTM on Dockerの概要
-------------------------
OpenRTM on Dockerに含まれるDockerイメージは　はDocker Engine上で動作するOSとOpenRTM-aistをまとめたコンテナです．
![Architecture of OpenRTM on Docker](../img/basic.png)

---

# 目次
- [使用方法](usage)
- [イメージ一覧](image)
- [サンプル](examples)
- [ツール](tools)

---

# リンク
## Docker Hub
[Docker Hub docker-openrtm](https://hub.docker.com/r/takahasi/docker-openrtm/)

## OpenRTM-aist
[OpenRTM-aist Web Page](http://www.openrtm.org/openrtm/)

## Dockerfile GitHub
[github docker-openrtm](https://github.com/takahasi/docker-openrtm)

## Web page
[OpenRTM on Docker Web Page](https://takahasi.github.io/docker-openrtm/)

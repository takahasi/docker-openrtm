[English](../index)

OpenRTM on Docker (docker-openrtm)
==================================
# **OpenRTM on Docker**って何？
**OpenRTM on Docker**は[OpenRTM-aist](http://www.openrtm.org/openrtm/)向けのDockerイメージです。

# 開発の動機
## OpenRTM-aistをもっと簡単に使いたい！
RTコンポーネント(RTC)を開発する場合、汎用性や後方互換製に配慮する必要があります。
そのためには、OSのバージョンやRTミドルウェアのバージョン、開発PCにインストールされている様々なライブラリとの依存関係を疎にする必要があります。
この作業、特に開発環境を整備することが非常に大変で、開発コストの増加に繋がります。
そこで、RTミドルウェアを含む様々なライブラリの組み合わせをDockerイメージとして提供することで、開発環境構築コストを低減できると考えました。

![Architecture of OpenRTM on Docker](../img/basic.png)

# 目次
* [使用方法](usage)
* [イメージ一覧](image)
* [サンプル](examples)

# リンク

## Docker Hub
[Docker Hub docker-openrtm](https://hub.docker.com/r/takahasi/docker-openrtm/)

## OpenRTM-aist
[OpenRTM-aist Web Page](http://www.openrtm.org/openrtm/)

## Dockerfile github
[github docker-openrtm](https://github.com/takahasi/docker-openrtm)

## Web page
[OpenRTM on Docker Web Page](https://takahasi.github.io/docker-openrtm/)

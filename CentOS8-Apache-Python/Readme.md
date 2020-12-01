# Docker + CentOS8 + Apache + Python

dockerでCentOS8環境を構築し、Apache・Pythonをインストール

## Step.1 使用するDocker Imageの取得

`Docker Hub`上にある公式の`centOS` imageを使用する。

```
# imageのpull
docker pull centos
```

## Step.2 Dockerfileの作成

pullしてきた`centos`のimageを元に、独自のimageを作成する`Dockerfile`を作成する。   
今回は`centOS8`を使用する為、`Dockerfile`に下記を記載し。imageを作成する。

```
FROM centos:8

RUN yum update -y && yum clean all

# Apache install
RUN yum install -y httpd
RUN yum install -y python3

EXPOSE 80

CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
```

`Dockerfile`では`apache`,`python3`のインストールを行い  
解放ポートの指定、`apache`のデタッチモードでの実行を行っている。

## Step.3 イメージの作成

先ほど作成した`Dockerfile`を元に、自作のイメージを作成する。

```
Docker build -t [imageの名前：タグ] [Dockerfileのディレクトリ]
```

## Step.4 コンテナの作成・立ち上げ

作成したイメージを元に、コンテナを作成・立ち上げる。

```
docker run -itd -v [ローカルのマウント元ディレクトリ]:/var/www/html --name [作成するコンテナ名] -p 8080:80 [元になるイメージ名]
```

※ `bash`を使用している場合ローカルのディレクトリの先頭に`/`を追加でつける必要がある。

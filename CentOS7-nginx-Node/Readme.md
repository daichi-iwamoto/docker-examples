# Docker + CentOS7 + Nginx + Node.js

dockerでCentOS7環境を構築し、Nginx・Node.jsをインストール

## Step.1 Dockerfileの作成

公式の`Ubuntu`のイメージを元に、`Dockerfile`を元に独自のイメージを作成する。  

```
FROM centos:7

RUN yum update -y && yum clean all
RUN yum -y install epel-release

# Node.js install
RUN yum install -y nodejs

# Nginx install
RUN yum install -y nginx

EXPOSE 80

# Nginx start
CMD ["nginx", "-g", "daemon off;"]
```

`Dockerfile`では`Node.js`,`Nginx`のインストールを行い、  
解放ポートの指定、`Nginx`のデタッチモードでの実行を行っている。

## Step.2 イメージの作成

先ほど作成した`Dockerfile`を元に、自作のイメージを作成する。

```
Docker build -t [imageの名前：タグ] [Dockerfileのディレクトリ]
```

## Step.3 コンテナの作成・立ち上げ

作成したイメージを元に、コンテナを作成・立ち上げる。

```
docker run -itd -v [ローカルのマウント元ディレクトリ]:/usr/share/nginx/html --name [作成するコンテナ名] -p 8080:80 [元になるイメージ名]
```

※ `bash`を使用している場合ローカルのディレクトリの先頭に`/`を追加でつける必要がある。

これでコンテナが立ち上がり、Pythonが使える仮想環境が作成される。  
http://localhost:8080/ を確認すると、テスト用の『index.html』が表示される。

コンテナ内に入りたい場合は下記で入ることが可能。  

```
docker exec -it [コンテナ名] bash
```

上記コマンドでコンテナ内に入ることで、ホストにインストールしていない`node`を使用することができる。

# Docker + Ubuntu + Apache + PHP

dockerでUbuntu環境を構築し、Apache・Pythonをインストール

## Step.1 Dockerfileの作成

公式の`Ubuntu`のイメージを元に、`Dockerfile`を作成する。   

```
FROM ubuntu

RUN apt-get update -y

# time zone setting
RUN apt-get install -y tzdata

# PHP install
RUN apt-get install -y php

# Apache install
RUN apt-get install -y apache2

EXPOSE 80

# Apache start
CMD ["apachectl","-D","FOREGROUND"]
```

`Dockerfile`では`apache`,`php`のインストールを行い  
解放ポートの指定、`apache`のデタッチモードでの実行を行っている。

## Step.2 イメージの作成

先ほど作成した`Dockerfile`を元に、自作のイメージを作成する。

```
Docker build -t [imageの名前：タグ] [Dockerfileのディレクトリ]
```

## Step.3 コンテナの作成・立ち上げ

作成したイメージを元に、コンテナを作成・立ち上げる。

```
docker run -itd -v [ローカルのマウント元ディレクトリ]:/var/www/html --name [作成するコンテナ名] -p 8080:80 [元になるイメージ名]
```

※ `bash`を使用している場合ローカルのディレクトリの先頭に`/`を追加でつける必要がある。

これでコンテナが立ち上がり、Pythonが使える仮想環境が作成される。  
コンテナ内に入りたい場合は下記で入ることが可能。

```
docker exec -it [コンテナ名] bash
```

上記コマンドでコンテナ内に入ることで、ホストにインストールしていないPHPを実行することが可能。

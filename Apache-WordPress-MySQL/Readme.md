# Docker + WordPress + MySQL

dockerでWordPressの開発環境を作成

## 使用方法

```
# イメージの作成
docker-compose build

# コンテナの作成・立ち上げ
docker-compose up -d
```

コンテナ内に入りたい場合は下記で入ることが可能。

```
docker exec -it [コンテナ名] bash
```
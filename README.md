# Dockerでの環境構築例

## よく使うコマンド

| コマンド | 内容 |
| --- | --- |
| docker ps [-a] | コンテナ一覧の表示 |
| docker rm [-f] [コンテナID] | コンテナの削除 |
| docker rmi [イメージ名] | イメージの削除 |
| docker build -t [イメージ名:タグ名] [dockerfileのディレクトリ] | dockerfileを元にイメージを作成する |
| docker run [-it] [-d] [p] [-v] [--name コンテナ名] [イメージ名] | 指定したイメージを元にコンテナを作成 |

# study-paiza

Paiza の課題に取り組むためのリポジトリ

## Docker 環境で Python を動かす手順

### 必要な環境

- Docker Desktop
- Docker Compose

### セットアップ手順

1. リポジトリをクローン

```bash
git clone https://github.com/otaki0413/study-paiza.git
cd study-paiza/python
```

2. Docker コンテナのビルドと起動

```bash
docker compose up -d --build
```

このコマンドは通常の開発時に使用します。Dockerfile に変更がない場合は既存のキャッシュを使用してビルドされます。

依存関係の問題が発生した場合やクリーンな状態から環境を構築したい場合は、以下のコマンドを使用します：

```bash
docker compose build --no-cache
docker compose up -d
```

3. コンテナに接続

```bash
docker compose exec app sh
```

4. Python の動作確認

```bash
python --version
```

### コンテナの停止

```bash
docker compose down
```

### 注意事項

- コンテナ内の `/code` ディレクトリがホストの `./python` ディレクトリにマウントされています
- ファイルの編集はホスト側で行い、実行はコンテナ内で行うことができます

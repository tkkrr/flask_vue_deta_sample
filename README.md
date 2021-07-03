# 実行方法
```bash
$ python main.py
```

# デプロイ方法
```bash
$ deta deploy
```

# コメント
flaskでvueを配信する場合は，アプリケーションの初期化時に
template_folderオプションを記述する必要がある．

DetaというサービスにはNoSQLのデータベースと，データドライブが提供される．
それぞれSQLにてアクセスするのだが，

# クラウドソーシングサイト スクレイピングソフト
## 概要
Crowd Worksなどのクラウドソーシングサイトで、新たな案件があった場合、Slackに通知してくるソフト

## 使い方

### 実行前のSlack通知設定
.envファイルを作成し、「incomig-webhook」アプリから通知させたいURLを指定してください。
```shell
SLACK_INCOMING_WEBHOOK_URL=https://hooks.slack.com/services/XXX.../YYY...
```

### 実行方法
```shell
docker compose up
```

### 検索ワードについて
検索にかけたいワードを、Dockerfileのsearch_wordで設定してください。
下記の例では、スクレイピングで検索する場合です。
```docker
CMD [ "scrapy", "crawl", "cw", "-a", "search_word=スクレイピング" ]
```

## 仕様・注意点
* Crowd Worksでの検索結果について、募集が終了しているものは除く


## 今後の展望
* 定期実行（毎日朝7時に実行）できるようにする
* 他のクラウドソーシングサイトにも対応させる（現状、Crowd Worksのみ）
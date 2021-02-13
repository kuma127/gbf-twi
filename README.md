# gbf-twi

## このツールについて

グラブルのTwitter救援IDを取得するためのツール  
Twitter上に貼られたIDをクリップボードに貼り付けるまでしか行わないので、  
所謂ゲームに直接介入するツールには該当しないと思われるが、  
使用は自己責任で

## 利用方法

### Twitter API アカウント取得

正規の方法に則りTwitter APIの認証情報を取得します。  
文献はたくさんあるので割愛

### 認証情報の配置

「credentials」ディレクトリの配下に「credentials.py」を作成し、  
その中でconsumer_key, consumer_secret, access_token, access_token_secretという変数を定義し  
それぞれの変数に該当するキーを文字列として定義すると使えるようになります

### モジュールのインストール

トップディレクトリで以下のコマンドを実行  
$ pip install -r requirements.txt

## search_akasha.py

アーカーシャ掘り専用モジュール  
実行すると最新ツイートからIDを抽出し、クリップボードにコピーする

## pyqt_akasha.py

search_akasha.pyの実行を  
PyQt5によって  
簡単なGUIによりボタンをポチッとするだけで実行できるようにしたもの

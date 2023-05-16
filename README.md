# Meet_station
複数の住所を半角コンマ区切りで入力していただくと、その中間地点の緯度経度、またその地点の最寄駅を表示します。家が離れている人との待ち合わせ場所決めに使ってみてください。

データは 「駅データ.jp」 様からダウンロードしております。

* URLは公開していないため、localhost でのみ閲覧可能です

# 使い方
1. git clone する
2. 必要なライブラリのインストール(geopy, geocoder など)
3. コマンドプロンプト（またはターミナル）で "python3 meet_station.py" を実行し、ローカルホストを立てる
4. ブラウザから "localhost:8000" に入る
5. 入力欄に "," （半角コンマ）区切りで市区町村名や有名な場所名を入力する

# 使用例
※「八王子市,新宿区,清水寺」を入力した例
![sample](https://github.com/tikiti-kyotaro/Meet_station/assets/88369097/a5d0694a-e922-4469-aceb-1cdbe8473705)

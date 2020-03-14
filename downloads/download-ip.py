# クジラAPI
# https://api.aoikujira.com/

# IP確認APIへアクセスして結果を表示する
# モジュールを取り込む
import urllib.request

# データを取得する
url = "https://api.aoikujira.com/ip/ini"
data = urllib.request.urlopen(url).read()

# バイナリーを文字列に変換
text = data.decode("utf-8")
print(text)

# データを取得
import requests
r = requests.get("https://uta.pw/shodou/img/3/3.png")

# バイナリー形式でデータを得る
with open("abc.png", "wb") as f:
    f.write(r.content)

print("saved")

import urllib.request

# URLとパスを保存
url = "https://uta.pw/shodou/img/28/214.png"
savename = "焼き鳥.png"

# ダウンロード
mem = urllib.request.urlopen(url).read()

# ファイルを保存
with open(savename, mode="wb") as f:
    f.write(mem)
    print('saved!')

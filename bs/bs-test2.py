# ライブラリを読み込む
from bs4 import BeautifulSoup

# 解析するHTML
html = """
<html><body>
    <h1 id="title">スクレイピングとは?</h1>
    <p id="body">Webページから任意のデータを抽出すること。</p>
</body></html>
"""

# HTMLを解析
soup = BeautifulSoup(html, 'html.parser')

# 取り出したい箇所を抽出する
title = soup.find(id="title")
body = soup.find(id="body")

# 要素のテキストを表示
print("#title = " + title.string)
print("#body = " + body.string)

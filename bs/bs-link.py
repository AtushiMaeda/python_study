# ライブラリを読み込む
from bs4 import BeautifulSoup

html = """
<html><body>
  <ul>
    <li><a href="http://uta.pw">uta</a></li>
    <li><a href="http://oto.chu.jp">uta</a></li>
  </ul>
</body></html>
"""

# HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

# find_all()メソッドで取り出す
links = soup.find_all("a")

# リンクを表示
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ":", href)


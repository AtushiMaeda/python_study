from bs4 import BeautifulSoup

# 対象となるHTML
html = """
<html><body>
<div id="maxim">
  <h1>トルストイの名言</h1>
  <ul class="sentences">
    <li>汝の心に教えよ、心に学ぶな</li>
    <li>謙虚な人はだれからも好かれる</li>
    <li>強い人々は、いつも気取らない</li>
  </ul>
</div>
</body></html>
"""

# HTMLを解析
soup = BeautifulSoup(html, 'html.parser')

# タイトル部分を取得
h1 = soup.select_one("div#maxim > h1").string
print("h1 =", h1)

# リスト部分を取得
li_list = soup.select("div#maxim > ul.sentences > li")
for li in li_list:
    print("li =", li.string)

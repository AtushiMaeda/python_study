from bs4 import BeautifulSoup
import urllib.request as req

url = "https://api.aoikujira.com/zip/xml/1500042"

# urlopen()でデータを取得
res = req.urlopen(url)

# BeautifulSoupで解析
soup = BeautifulSoup(res, "html.parser")

# 取り出したいデータを抽出
prefecture = soup.find("ken").string
city = soup.find("shi").string
town = soup.find("cho").string

print(prefecture, city, town)

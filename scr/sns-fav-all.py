from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USER = "JS-TESTER"
PASS = "ipCU12ySxI"
FAV_USER_ID = 32
SNS_URL = "https://uta.pw/sakusibbs/"

# Firefoxのドライバーを得る
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

# ログインする
url_login = SNS_URL + "users.php?action=login"
browser.get(url_login)

# テキストボックスに文字を入力してフォームを送信する関数
def form_post(frm, d):
    for field, value in d.items():
        e = frm.find_element_by_name(field)
        e.clear()
        e.send_keys(value)
    frm.submit()
    # ページのロード完了まで待機
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin"))
    )

# 対象となるフォームを設定
frm = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/form")
# テキストボックスにデータを指定して送信する
form_post(frm, {
    "username_mmlbbs6": USER,
    "password_mmlbbs6": PASS})

# 本当にログインしたか画像で確認してみる
browser.save_screenshot("sns-logined.png")
# 本当にログインしたかHTMLで判断してみる
e = browser.find_element_by_id("bbsheader")
html = e.get_attribute("innerHTML")
if html.find("action=logout") < 0:
    print("ログインできません")
    quit()
print("ログインしました")
time.sleep(1)

# ユーザーの作品一覧ページを開く
url = SNS_URL + "users.php?user_id=" + str(FAV_USER_ID)
browser.get(url)

# 作品一覧を得る
sakuhin_list = []
links = browser.find_elements_by_css_selector("ul#mmlist li a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    sakuhin_list.append((href, title))
print("+ 作品一覧を{0}件取得しました".format(len(sakuhin_list)))

# 一気にお気に入りをつける

for href, title in sakuhin_list:
    # 作品ページを開く
    print("-", title)
    browser.get(href)
    try:
        # お気に入りボタンを得る
        # e = browser.find_element_by_id("fav_add_btn")
        # e.click()
        # お気に入りを取り消す場合
        e = browser.find_element_by_id("fav_remove_btn")
        e.click()
        print("| お気に入りしました")
    except:
        # お気に入りボタンが無かったとき
        print("| すでにお気に入りでした")
    # 負荷軽減
    time.sleep(1)

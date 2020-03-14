from selenium.webdriver import Firefox, FirefoxOptions

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# Firefoxのヘッドレスモードを有効にする
options = FirefoxOptions()
options.add_argument('-headless')

# FireFoxを起動する
browser = Firefox(options=options)

# URLを読み込む
browser.get(url)

# 画面をキャプチャーしてファイルに保存
browser.save_screenshot("website.png")
# ブラウザを終了
browser.quit()

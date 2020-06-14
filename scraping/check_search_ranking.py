import time

from selenium import webdriver

# headless環境で動かす際の設定
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome('/Applications/chromedriver', options=options)

# 必要に応じ、chromedriverのパスを書き換えて下さい
driver = webdriver.Chrome('/Applications/chromedriver')

driver.get('XXXXX')
time.sleep(1)
search_box = driver.find_element_by_name('q')
# 任意の検索したいキーワードを指定
search_box.send_keys('XXXXX')
time.sleep(1)
search_box.submit()
time.sleep(1)
results = driver.find_elements_by_css_selector('div.r h3')

for index, result in enumerate(results):
    print('検索順位{}位のサイトは: '.format(index + 1) + result.text)
    if index == 4:
        break

driver.quit()

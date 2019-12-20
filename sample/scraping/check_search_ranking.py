import time
from selenium import webdriver

# 必要に応じ、chromedriverのパスを書き換えて下さい
driver = webdriver.Chrome('/Applications/chromedriver')

driver.get('XXXXX')
time.sleep(1)
search_box = driver.find_element_by_name('q')
search_box.send_keys('XXXXX')
time.sleep(1)
search_box.submit()
time.sleep(1)
results = driver.find_elements_by_css_selector('div.r h3')
driver.save_screenshot('screenshot.png')

for index, result in enumerate(results):
    print('検索順位{}位のサイトは: '.format(index + 1) + result.text)
    if index == 4:
        break

driver.quit()

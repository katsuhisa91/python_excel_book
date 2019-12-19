import time
from selenium import webdriver

driver = webdriver.Chrome('/Applications/chromedriver')

driver.get('http://www.google.com/')
time.sleep(3)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
time.sleep(3)
search_box.submit()
time.sleep(3)
driver.quit()

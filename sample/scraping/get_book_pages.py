import requests
import time

for page_num in range(4):
    url = 'xxxxxx&page={}'.format(page_num)
    r = requests.get(url)
    html = r.text
    print(html)
    time.sleep(1)

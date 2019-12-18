import requests
import time

for page_num in range(4):
    url = 'xxxxx'
    params = {
        'g': 'プログラミング・システム開発',
        'page': page_num
    }
    r = requests.get(url, params)
    print(r.url)
    html = r.text
    time.sleep(1)

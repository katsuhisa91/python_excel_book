import requests
import time

for page_num in range(4):
    # url = 'https://gihyo.jp/book/genre?g=プログラミング・システム開発&page=' + str(page_num)
    # でもOK
    url = 'https://gihyo.jp/book/genre?g=プログラミング・システム開発&page={}'.format(page_num)
    r = requests.get(url)
    html = r.text
    print(html)
    time.sleep(1)

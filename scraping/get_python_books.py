import time

import requests
from bs4 import BeautifulSoup

for page_num in range(4):
    url = 'https://gihyo.jp/book/genre'
    params = {
        'g': 'プログラミング・システム開発',
        'page': page_num
    }
    r = requests.get(url, params)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    book_elems = soup.select('#mainbook > ul > li > div.data > h3 > a')

    for book_elem in book_elems:
        book_title = book_elem.text
        if 'Python' in book_title:
            print(book_title)
            book_url = book_elem.get('href')
            print('https://gihyo.jp' + book_url)

    time.sleep(1)

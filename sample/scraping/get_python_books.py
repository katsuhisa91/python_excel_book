import requests
from bs4 import BeautifulSoup
import time

for page_num in range(4):
    url = 'xxxxxx&page={}'.format(page_num)
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    book_list = soup.select('div.data > h3 > a')

    for book in book_list:
        book_title = book.text
        if 'Python' in book_title:
            print(book_title)
            book_url = book.get('href')
            print('https://gihyo.jp' + book_url)

    time.sleep(1)

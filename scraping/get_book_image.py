import requests
from bs4 import BeautifulSoup

url = 'xxxxx'
params = {
    'g': 'プログラミング・システム開発',
    'page': 0
}
r = requests.get(url, params)
html = r.text
soup = BeautifulSoup(html, 'lxml')
book_img_elems = soup.select('#mainbook > ul > li > div.cover > a > img')
book_img_elem = book_img_elems[0]

img = requests.get('xxxxx' + book_img_elem.attrs['data-src'])

with open('.\\book.jpg', 'wb') as f:
    f.write(img.content)

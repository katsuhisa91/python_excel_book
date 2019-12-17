from bs4 import BeautifulSoup

with open('sample.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
text = soup.find(style="color:red;").text
print(text)

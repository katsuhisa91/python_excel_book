from bs4 import BeautifulSoup

with open('sample.html') as f:
    soup = BeautifulSoup(f, 'lxml')

text = soup.find(style="color:red;").text
print(text)

from bs4 import BeautifulSoup

xml = """
<?xml version="1.0"?>
<sample>
    <data>1</data>
    <data>2</data>
</sample>
"""

soup = BeautifulSoup(xml, 'xml')
elems = soup.find_all('data')
print(elems)

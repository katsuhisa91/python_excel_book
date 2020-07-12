import re

with open('.\\file.txt', encoding = 'UTF-8') as f:
    text_mod = re.sub('東京', 'Tokyo', f.read())
    print(text_mod)

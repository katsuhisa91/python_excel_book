import re

with open('.\\file.txt', encoding = 'UTF-8') as f:
    postal_code_list = re.findall(r'\d\d\d-\d\d\d\d', f.read())

print(postal_code_list)

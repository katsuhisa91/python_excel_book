import re

with open('./file.txt') as f:
    postal_code_list = re.findall(r'\d\d\d-\d\d\d\d', f.read())

print(postal_code_list)

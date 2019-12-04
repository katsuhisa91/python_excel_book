import re

postal_code_regex = re.compile(r'\d\d\d-\d\d\d\d')
# こちらと同義
# postal_code_regex = re.compile(r'\d{3}-\d{4}')

with open('./file.txt') as f:
    postal_code_list = postal_code_regex.findall(f.read())

print(postal_code_list)

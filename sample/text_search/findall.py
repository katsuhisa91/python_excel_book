import re

postal_code_regex = re.compile(r'\d\d\d-\d\d\d\d')

with open('./file.txt') as f:
    postal_code_list = postal_code_regex.findall(f.read())

print(postal_code_list)

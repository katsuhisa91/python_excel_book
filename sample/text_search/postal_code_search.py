import re

postal_code_regex = re.compile(r'\d\d\d-\d\d\d\d')

with open('./file.txt') as f:
    postal_code_match = postal_code_regex.search(f.read())

if postal_code_match:
    print(postal_code_match)
    print(postal_code_match.group())

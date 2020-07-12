import re

postal_code_regex = re.compile(r'\d\d\d-\d\d\d\d')

with open('.\\file.txt', encoding = 'UTF-8') as f:
    postal_code_match = postal_code_regex.search(f.read())

if postal_code_match:
    print(postal_code_match)
    print(postal_code_match.group())
    print(postal_code_match.start())
    print(postal_code_match.end())
    print(postal_code_match.span())

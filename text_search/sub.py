import re

with open('./file.txt', newline='') as f:
    text_mod = re.sub('東京', 'Tokyo', f.read())
    # 以下のように正規表現も使えます
    # text_mod = re.sub('.京', 'Tokyo', f.read())
    print(text_mod)

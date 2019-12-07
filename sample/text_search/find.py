with open('./file.txt', newline='') as f:
    text = f.read()

if 'タワー' in text:
    fd = text.find('タワー')
    print('タワーという文字列が' + str(fd + 1) + '字目に含まれています')
else:
    print('タワーという文字列は含まれていません')

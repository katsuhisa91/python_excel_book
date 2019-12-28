sample_list = [1, 2, 3]

try:
    input_num = int(input('取り出したい値を教えて下さい: '))
except ValueError as e:
    print('catch ValueError:', e)

try:
    print(sample_list[input_num])
except IndexError as e:
    print('catch IndexError:', e)

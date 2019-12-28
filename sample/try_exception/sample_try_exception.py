sample_list = [1, 2, 3]
input_value = input('取り出したい値を教えて下さい: ')

try:
    print(sample_list[int(input_value)])
except IndexError as e:
    print('catch IndexError:', e)
except ValueError as e:
    print('catch ValueError:', e)

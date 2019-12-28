sample_list = [1, 2, 3]

try:
    input_num = int(input('取り出したい値を教えて下さい: '))
except ValueError as e:
    print('数字を入力してください')

try:
    print(sample_list[input_num])
except IndexError as e:
    print('リストには値が3つしか入っていないので、0〜2の値を指定してください')

fruits = ['apple', 'orange', 'banana' ]
input_value = input('取り出したいフルーツの番号を教えてください: ')

try:
    print(fruits[int(input_value)])
except IndexError as e:
    print('catch IndexError:', e)
except ValueError as e:
    print('catch ValueError:', e)

money = int(input('何円持っている？：'))
if money > 500:
    print('卵と牛乳とパンを買いましょう')
elif money > 300:
    print('卵と牛乳を買いましょう')
else:
    print('牛乳を買いましょう')

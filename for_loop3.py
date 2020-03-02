fruits = ['apple', 'orange', 'banana', 'grape']
for i, fruit in enumerate(fruits):
    print(i, fruit)
    if i == 2:
        break

x = []
y = []
x, y = enumerate(fruits)
print(x, y)

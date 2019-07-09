fruit_list = ['банан', 'апельсин', 'мандарин', 'вишня', 'арбуз', 'виноград', 'ананас']

for i in enumerate(fruit_list, 1):
    print (i)

b = {'a', 'b', 'c', 'c', 'a', 'e', 'd'}
d = {'a', 'b', 'c'}
c = b - d
print(list(c))
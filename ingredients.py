ingredients = ['snails', 'leeches', 'gorilla belly-bottem lint', 'caterpillar eyebrows', 'centipede toes']
index = 0
for i in ingredients:
    index = index + 1
    print('%d %s' % (index, i))

for i, v in enumerate(ingredients):
    print('%d %s' % (i + 1, v))

for v in enumerate(ingredients):
    print(v)
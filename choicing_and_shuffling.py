import imp
import random
import time

random.seed(time.time())
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))

random.shuffle(desserts)
print(desserts)
import random

num = random.randint(1, 100)
print('I\'m thinking of a number between 1 and 100...')
while True:
    guess = input()
    i = int(guess)
    if i == num:
        print('Well done! You\'re right already!')
        break
    elif i < num:
        print('Try higher:')
    elif i > num:
        print('Try lower:')
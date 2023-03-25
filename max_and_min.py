import random

guess_this_number = random.randint(0, 10)
player_guesses = []
for x in range(0,4):
    number = input('Enter a number: ')
    player_guesses.append(int(number))
if max(player_guesses) > guess_this_number:
    print('Boom! You lose!')
else:
    print('You win!')
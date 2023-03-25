import sys


def silly_joke():
    print('How old are you?')
    age = int(sys.stdin.readline())
    if age >= 4 and age <= 14:
        print('What\'s math problem\'s other name? A headache!')
    else:
        print('Emm...')

silly_joke()
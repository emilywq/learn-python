# your_age = input('Enter your age:')
# while not bool(your_age.rstrip()):
#     your_age = input('Enter your age:')
# if bool(your_age.rstrip()):
#     age = float(your_age)
# if age < 14:
#     print('You\'re  %f years younger than me!' % (14 - age))
# elif age > 14:
#     print('You\'re %f years older than me!' % (age - 14))
# elif age == 14:
#     print('You\'re the same age as me!')

while True:
    your_age = input('Enter your age: ')
    if not your_age.rstrip():
        continue
    age = int(your_age)
    if age < 14:
        print('You\'re  %d years younger than me!' % (14 - age))
    elif age > 14:
        print('You\'re %d years older than me!' % (age - 14))
    elif age == 14:
        print('You\'re the same age as me!')
    break
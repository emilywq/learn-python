weight_on_earth = 45
for x in range(0, 16):
    weight_on_earth = weight_on_earth + 1
    weight_on_moon = weight_on_earth * 0.165
    print(weight_on_moon)

def weight_year(earth_weight):
    for x in range(0, 16):
        earth_weight = earth_weight + 1
        moon_weight = earth_weight * 0.165
        print('Your weight on the moon is %s this year!' % moon_weight)

weight_year(45)

def moon_weight(inital_moon_weight, increased_moon_weight):
    for year_passed in range(0, 16):
        recent_moon_weight = inital_moon_weight + increased_moon_weight * year_passed
        print('Your weight on the moon is %s this year!' % recent_moon_weight)

moon_weight(7, 0.165)

def moon_weight(inital_moon_weight, increased_moon_weight, year_passed):
    for year_passed in range(0, 16, 5):
        recent_moon_weight = inital_moon_weight + increased_moon_weight * year_passed
        print('Your weight on the moon is %s this year!' % recent_moon_weight)

moon_weight(7, 0.165, 5)

def moon_weight(inital_moon_weight, increased_moon_weight, years):
    for year_passed in range(0, years+1):
        recent_moon_weight = inital_moon_weight + increased_moon_weight * year_passed
        print('Your weight on the moon is %s this year!' % recent_moon_weight)

moon_weight(7, 0.165, 15)

import sys

def weight_year():
    print('Please enter your current Earth weight')
    earth_weight = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    increased_weight = float(sys.stdin.readline())
    print('Please enter the number of years')
    years_passed = int(sys.stdin.readline())
    for x in range(0, years_passed):
        earth_weight += increased_weight * x
        moon_weight = earth_weight * 0.165
        print('Your weight on the moon is %f this year!' % moon_weight)

weight_year()
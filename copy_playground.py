import copy

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

# harry = Animal('hippogriff', 6, 'pink')
# harriet = copy.copy(harry)
# print(harry.color)
# print(harriet.color)

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('blgill', 0, 'pasiley')
my_animals = [harry, carrie, billy]
# more_animals = copy.copy(my_animals)
# print(more_animals[0].species)
# print(more_animals[1].species)

# my_animals[0].species = 'ghoul'
# print(my_animals[0].species)
# print(more_animals[0].species)

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)
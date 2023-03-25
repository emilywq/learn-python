class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalk(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print('I\'ve found food!')
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        for x in range(0, 4):
            self.move()
    def __init__(self, spots, legs):
        self.giraffe_spots = spots
        self.giraffe_legs = legs
    def left_foot_forward(self):
        print('left foot forward')
    def right_foot_forward(self):
        print('right foot forward')
    def left_foot_backward(self):
        print('left foot backward')
    def right_foot_backward(self):
        print('right foot backward')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_backward()

# reginald = Giraffes()
# reginald.move()
# reginald.eat_leaves_from_trees()

# harold = Giraffes()
# harold.find_food()
# harold.dance_a_jig()

# ozward = Giraffes(100, 4)
# gertrude = Giraffes(150, 4)
# print(ozward.giraffe_spots, ozward.giraffe_legs)
# print(gertrude.giraffe_spots, gertrude.giraffe_legs)

reginald = Giraffes(100, 4)
reginald.dance()
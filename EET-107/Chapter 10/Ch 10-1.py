# Sean Kelley
# Ch10-1
# 20 July 2021

class Vehicle:
    def __init__(self, givenmake, givencolor, givenspeed):
        self.make = givenmake
        self.color = givencolor
        self.speed = givenspeed
    def accelerate(self):
        self.speed += 1
    def deccelerate(self):
        self.speed -= 1
    def displayspeed(self):
        print('Accelerating...')
        print(f'Current speed: {self.speed}')


v1 = Vehicle('Lexus', 'White', 0)
v1.accelerate()
v1.displayspeed()
v1.accelerate()
v1.displayspeed()
print()
v1.deccelerate()
v1.displayspeed()
v1.deccelerate()
v1.displayspeed()


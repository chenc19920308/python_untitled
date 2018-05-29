import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(1,10)
        self.y = r.randint(1,10)
        # print(self.x,self.y)
    def move(self):
        self.x -= 1
        self.y -= 1
        return (self.x, self.y)

class Shark(Fish):
    pass

shark = Shark()
fish = Fish()

print(shark)
print(shark.__dict__)
print(shark.move())
print(shark.move())
print(shark.move())
print(shark.__dict__)
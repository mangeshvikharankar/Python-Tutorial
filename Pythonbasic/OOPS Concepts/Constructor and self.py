
class Computer:
    def __init__(self):
        self.name = " mangesh"
        self.age = 25

    def compare(self,others):
        if self.age == others.age:
            return True
        else:
            return False

c1 = Computer()
c1.age  = 30
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are diffrent")

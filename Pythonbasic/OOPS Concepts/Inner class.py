

class student:                       #Outer class

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(s1.name,s1.rollno)
        self.lap.show()

    class laptop:                   #Inner class

        def __init__(self):
            self.name = 'HP'
            self.ram = 8

        def show(self):
            print(self.name, self.ram)

s1 = student('mangesh',2)

s1.show()


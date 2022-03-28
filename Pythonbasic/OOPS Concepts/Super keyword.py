
# Super keyword is used to access all metods or constrctor of superclass from subclass
#Method Resolution Order(MRO) -  When we call subclass object using super keyword it calls from left hand first.
class A:

    def __init__(self):
        print("Constructor of class A")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A):

    def __init__(self):
        super().__init__()
        print("Constructor of class B")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

a1 = B()


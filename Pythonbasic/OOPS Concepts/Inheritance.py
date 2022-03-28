
# Single level inheritance - One subclass or childclass acquires property of One superclass or parentclass.

class A:

    def __init__(self):
        print("Constructor of class A")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A):       # class B(subclass or child class) inherites all the properties of class A(superclass or parent class)

    def __init__(self):
        print("Constructor of class B")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

print("=======================================================")

# Multi level inheritance - One subclass or childclass acquires property of One superclass or parentclass. and this superclass acquires property of his superclass.

class S:
    def team1(self):
        print("team1 is active")

s1 = S()
s1.team1()

class T(S):
    def team2(self):
        print("team1 is active")

t1 = T()
t1.team1()
t1.team2()

class U(T):
    def team3(self):
        print("team1 is active")

U1 = U()

U1.team1()
U1.team2()
U1.team3()

print("=======================================================")

# Multiple inheritance  - More than one subclass acquires property of one superclass.

class X:
    def comp1(self):
        print("comp1 is very slow")

x1 = X()
x1.comp1()

class Y:
    def comp2(self):
        print("comp2 is very slow")

y1 = Y()
y1.comp2()

class Z(X,Y):
    def comp3(self):
        print("comp3 is very slow")

z1 = Z()
z1.comp1()
z1.comp2()
z1.comp3()








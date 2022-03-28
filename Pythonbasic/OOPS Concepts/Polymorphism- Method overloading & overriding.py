# Polymorphism: One thing behave in multiple ways

# 3. Method Overloading - is not supports in python but you can define a method in such a way that there are multiple ways to call it

class Student:

    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s =a
        return s

s1 = Student()

print(s1.sum())

print("=================================")
# 4. Method Overriding- when you have two methods with the same name that each perform different tasks

class A:
    def teamA(self):
        print("team A wins")
class B:
    def teamB(self):
        print("team B wins")

obj = B()
obj.teamB()
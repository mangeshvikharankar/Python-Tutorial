
# Abstract class - A class which have abstract method is called as Abstarct class.a class is called abstract class only if it has at least one abstract method.
# Abstract method -  A method which is having declaration but not defination (body) is called as Abstract method.
# We cannot create object of abstract class. i.e. we Can't instantiate abstract class with abstract method.
# when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.if it is not done then child class also becomes abstract class automatically.
# at last, python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract.
from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Whiteboard():
    def write(self):
        print("writing on board")

class Laptop(Computer):
    def process(self):
        print("method is running")

class Programmer():
    def work(self,com):
        print("solving bugs")
        com.process()

obj1 = Laptop()
obj2 = Whiteboard()

prog = Programmer()
prog.work(obj2)

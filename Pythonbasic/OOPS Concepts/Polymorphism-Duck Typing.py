

# Polymorphism: One thing behave in multiple ways
# 1. Duck Typing
# 2. Operator overloading
# 3. Method Overloading
# 4. Method Overriding

# 1. Duck Typing:(Interface)
class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class Myeditor:
    def execute(self):
        print("running")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
         ide.execute()

ide = Myeditor()
lap1 = Laptop()
lap1.code(ide)










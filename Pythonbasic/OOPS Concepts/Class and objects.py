
# class we can called as a design or blueprint
class computer:

    def config(self):
        print("i5, 4th g4n, 4gb ram")

# objects are instance of class
# objects are having attributes and behaviour
com1 = computer()
com2 = computer()

computer.config(com1)
computer.config(com2)

#simple way to call an object
com1.config()

a = 5
a.bit_length()


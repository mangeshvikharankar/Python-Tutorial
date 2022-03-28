# Types of variables:
# 1. class (Static) variable
# 2. Instance (Non static) variable

class Car:
     wheels = 4  # Static variable

     def __init__(self):
         self.mil = 8   # non static variable
         self.com = "BMW"

C1 = Car()
C2 = Car()

C1.mil = 8

Car.wheels = 5

print("Company = ",C1.com, "Mileage = ",C1.mil , "Wheels = ",Car.wheels)
print("Company = ",C2.com, "Mileage = ",C2.mil , "Wheels = ",Car.wheels)





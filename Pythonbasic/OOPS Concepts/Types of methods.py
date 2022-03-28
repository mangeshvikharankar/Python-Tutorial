
# Types of methods
# 1. Instance method
# 2. Class method
# 3. Static method

class student:

    school = "pethe"    # class variable

#1. Instance method

    def __init__(self,m1,m2,m3):
        self.m1 = m1    #Instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3


s1 = student(10,20,30)
print(s1.avg())

#2. Class method

@classmethod      #decorator
def info(cls):
    return cls.school
print(student.school)


#3. static methods:
@staticmethod
def get_age(age):
    if age >17:
        print("belongs to school")
    else:
        print("not belongs to school")

student.get_age(16)





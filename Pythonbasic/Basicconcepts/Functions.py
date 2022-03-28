
def demo():
    print("hello")
    print("mangesh")
demo()
print("============")

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2 = add_sub(4,2)
print(result1, result2)
print("============")

# types of arguments:-

#1.Position arguments
def person(name,age):
    print(name)
    print(age)
person('mangesh',25)
print("============")

#2. Keyword arguments:
def person(name,age):
    print(name)
    print(age)
person(age=25, name='sumit')
print("============")

#3. default arguments:
def person(name,age=18):
    print(name)
    print(age)
person('ashish')
print("============")

#4. Keyword arguments:

def person(name,*data):
    print(name)
    print(data)

person('anket', 26, 'nashik', 73393933)
print("============")

#5. keyword variable length arguments:

def person(name,**data):
    print(name)
    print(data)

person('anket', age=26, city='nashik', mob=73393933)
print("============")





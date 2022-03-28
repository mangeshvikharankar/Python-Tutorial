#if statement:
if True:
    print("I am right")
if False:
    print("I am wrong")
print("================")

# if else statement:
x = 7
r = x % 2

if r==0:
    print("Given number is even")
else:
    print("Given number is odd")
print("End")
print("================")

#if if-else statement (Nested-if):
a = 8
b = a % 2
if (b==0):
    print("Given number is even")
    if a<10:
        print("a is greater")
    else:
        print("a is smaller")
else:
    print("Given number is odd")
print("================")

# elif statement:
z =3
if z==1:
    print("one")

elif z==2:
    print("Two")

elif z==3:
    print("Three")

elif z==4:
    print("Four")
else:
    print("wrong input")







from numpy import*
#Ways of creating array in numpy:

#First way- array()
given1 = array([1,2,3,4,5],int)
for a in given1:
    print(a)
print("===========")

#Second way- linspace()
given2 = linspace(0,15,5)
for b in given2:
    print(b)
print("===========")

#Third way - logspace()
given3 =logspace(0,15,5)
for c in given3:
    print(c)
print("===========")

#Fourth way - arange()
given4 = arange(1,15,2)
for d in given4:
    print(d)
print("===========")

#fifth way - zeros()
given5 = zeros(5,int)
for e in given5:
    print(e)
print("===========")

#Sixth way - ones()
given6 = ones(5,int)
for f in given6:
    print(f)
print("===========")


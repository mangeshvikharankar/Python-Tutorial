from array import *

vals = array('i', [5,9,8,4,2])

for i in range(len(vals)):
    print(vals[i])

print("==================")

 # or

for a in vals:
    print(a)

print("==================")
vals.reverse()
print(vals)

print(vals.buffer_info())

print(vals.typecode)

print ("======")

newarr = array(vals.typecode, (a for a in vals))

for e in newarr:
    print(e)


from numpy import*

given = array([[1,2,3,4,5,6],[4,5,6,7,8,9]])
#print(given)
for a in given:
    print(a)

print(given.dtype)   # data
print(given.ndim)    # no. of dimension or ranking
print(given.shape)   #shape
print(given.size)    #size
print("===========")

#covert multidimesnional into single dimensional
given2 = given.flatten()
for b in given:
    print(b)
print(given2.ndim)
print("===========")

#covert single dimensional array into three dimensional
given3=given2.reshape(3,4)
for z in given3:
    print(z)






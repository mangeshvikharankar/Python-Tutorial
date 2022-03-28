from numpy import*

given1 = array([1,2,3,4,5])

given2 = array([6,7,8,9,10])

given = given1 +given2

#given = given +5

print(given)

print("============")

#Mathmatical operations:

new = array([80,50,10,20,30,40,50])

print ("sin", sin(new))

print("sum", sum(new))

print("sqrt", sqrt(new))

print(max(new))
print("============")

#Copying an array

arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()

arr1[1] = 7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


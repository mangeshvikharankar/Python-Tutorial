from array import*

given = array('i', [])

n = int(input("Enter the length of array"))

for i in range(n):
    x = int(input("Enter the next value"))
    given.append(x)

for a in given:
    print(a)

# Manually Value search for index position
index =int(input("Enter the value for search"))

k=0
for z in given:
    if z==index:
        print(k)
        break
    k+=1

#Seach index value by method
print (given.index(index))

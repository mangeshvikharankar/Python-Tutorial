
#search for a number by while loop:

pos = -1
def search(list1,n):
    i = 0
    while i<len(list1):
        if list1[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

list1 = [1,2,3,4,5]
n = 4

if search(list1,n):
    print("found at position ", pos)
else:
    print("not found")

print("=======================")

#search for a number by for loop:
list2 = [10,20,30,40,50]
given = int(input("Enter a number to find"))
i = 0
def search2(list2,given):
    for i in range(len(list2)):
        if list2[i] == given:
            return True
        return False
if search(list2,given):
    print("found at position")
else:
    print("Not found")






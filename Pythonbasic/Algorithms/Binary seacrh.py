
# For binary search we required sorted values of list
pos = -1
def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid +1
            else:
                u = mid-1
    return False

list= [10, 20, 30 ,40, 100]
n = int(input(" Enter a number to found"))

if search(list, n):
    print("Found at position ", pos)
else:
    print("not found")

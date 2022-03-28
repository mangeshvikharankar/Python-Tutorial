
def count(given):
    even = 0
    odd = 0

    for i in given:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

given = [10,13,15,48,390,47,89,3,30,45]

even,odd = count(given)
print("even : {} and odd : {}".format(even, odd))
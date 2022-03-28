

from functools import reduce
# Filter using lambda
nums = [3,2,4,5,6,7,8,9]

evens = list(filter(lambda n : n % 2 == 0, nums))

print (evens)

# Map using lambda

doubles = list(map(lambda n : n * 2,evens))

print(doubles)

# Reduce using lambda

sum = reduce(lambda a , b : a + b, doubles)

print(sum)

nums = [1,2,3,4,5,6]

it = iter(nums)
print(it.__next__())


# Program to find top ten value by iterator

class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

output = Topten()

for i in output:
    print (i)




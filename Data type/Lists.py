
nums = [1,2,3,4,5,6]

print(nums)
print(nums[0])
print(nums[4])
print(nums[2:4])
print(nums[2:])
print(nums[-5])

print('min', min(nums))
print('max', max(nums))
print('sum', sum(nums))

nums.append(20)
print('append',nums)

nums.insert(2,100)
print('insert',nums)

nums.remove(100)
print('remove',nums)

nums.pop(1)
print('pop', nums)

del nums[2:]
print('del', nums)

nums.extend([4,5,6,7,8,9,0])
print('extend', nums)

print("=================================")
names= ['mangesh', 'ashish','vitthal']
print(names)

mix = [nums, names]
print('mix', mix)
demo = ['mangesh', 9.4, 'abc']
print(demo)

test= [347,5858,29,48494,666]
test.sort()
print(test)

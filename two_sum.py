nums = [2, 7, 11, 15, 1]
target = 3

my_map = {}

for i in range(len(nums)):
    my_map[nums[i]] = i
    diff = target - nums[i]
    if diff in my_map:
        print(i, my_map[diff])

    

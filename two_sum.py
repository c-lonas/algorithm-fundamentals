nums = [2, 7, 11, 15, 1]
target = 3

my_map = {}

for i in range(len(nums)):
    my_map[nums[i]] = i
    x = target - nums[i]

    if x in my_map and my_map[x] != i:
        print(i, my_map[x])

    

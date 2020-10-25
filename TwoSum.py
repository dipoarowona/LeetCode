def twoSum(nums, target):
    items = {}
    for x,y in enumerate(nums):
        newTarget = target - y 
        if newTarget in items:
            return [x,items[newTarget]]
        else: 
            items[y] = x


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
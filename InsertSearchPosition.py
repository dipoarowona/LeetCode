def searchInsert(nums, target):
    nums.sort()
    
    start = 0
    end = len(nums)
    index = 0
    if target in nums:
        while start<end:
            mid = int((start+end)/2)
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
    
    for i in range(len(nums)):
        if nums[i] < target:
            continue 
        else:
            return i
    return len(nums)

print(searchInsert([1,3,5,6],7))
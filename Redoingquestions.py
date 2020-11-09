#redoing to sum from memory 
def TwoSum(lst, x):
    
    data = {}

    for index,item in enumerate(lst):
        difference = abs(x-item)


        if difference in data:
             return [index,data[difference]]
        else:
            data[item] = index
    return -1


print(TwoSum([3,3,12,5,63,67,7,33,6,73,57,3,23],14))
class Solution(object):
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeats = {}
        for i in nums:
            if i in repeats.keys():
                repeats[i]+=1
                if repeats[i] >=2:
                    repeats.pop(i)  
            else:
                repeats[i] = 1
        # index = repeats.values().index(1)
        return repeats.keys()[0]
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeats = []
        for i in nums:
            if not i in repeats:
                repeats.append(i)
            else:
                repeats.remove(i)

        return repeats[0]
                
#Solution 1 using Map
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {} #hashmap
        for i,x in enumerate(nums):
            y = target-x
            if y in d:
                return [d[y],i]
            d[x] = i
            
        return []
        

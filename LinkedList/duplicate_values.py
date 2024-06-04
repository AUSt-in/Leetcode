class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        for num in nums:
            if num in dictionary:
                return num
            
            else:
                dictionary[num] =1
            
        return -1

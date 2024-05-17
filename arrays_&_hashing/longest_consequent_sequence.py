class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # If nums is empty
            return 0
        
        # Sort the elements
        nums.sort()
        
        # Initialize variables
        n = len(nums)
        curr = 1  # Current consecutive length
        longest = 1  # Longest consecutive length
        
        # Iterate through the sorted array
        for i in range(1, n):
            # Check if the current element is consecutive to the previous element
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            # If not consecutive, update the longest consecutive length
            elif nums[i] != nums[i - 1]:
                longest = max(longest, curr)
                curr = 1  # Reset current consecutive length
        
        # Update longest consecutive length in case the last sequence is the longest
        longest = max(longest, curr)
        
        return longest

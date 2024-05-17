class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # what I know: each element of result array is product of other elements
        # what case can I face problem: take for example an element in input array is 0
        # what most students do: multiply all elements and divide by the the element in input   array
        # first multiplying with previous elements
        # then multiplying with elements next to that
        # multiplying the previous and later elements 
        # O (n+n) = O(n)
        # take some more constant space
        # optimal: doing it with a single array
        # what I know is doing with two arrays first
        n = len(nums)
        arr_before = [1] * n
        arr_after = [1]* n
        result = [1]*n
        for i in range(1, n):
            arr_before[i] = arr_before[i - 1] * nums[i - 1]
        
        # Calculate products of elements after each element
        for i in range(n - 2, -1, -1):
            arr_after[i] = arr_after[i + 1] * nums[i + 1]
        
        # Combine products from both arrays to get the final result
        for i in range(n):
            result[i] = arr_before[i] * arr_after[i]
        
        return result

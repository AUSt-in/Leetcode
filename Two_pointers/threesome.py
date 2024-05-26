class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        #Solving Question in O(n*2)
        for idx, point in  enumerate(nums):
            if idx > 0 and point == nums[idx - 1]: #skipping duplicate values to optimize
                continue
            i = idx+1
            j= len(nums) -1

            while(i<j):
                total = point + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    result.append([point, nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1  # Skip duplicates for nums[i]
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1  # Skip duplicates for nums[j]
                    i += 1
                    j -= 1
        
        return result

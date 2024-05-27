class Solution:
    def trap(self, height: List[int]) -> int:
        #using two pointers, main point to note is cube is one 
        #using o(n*2) solution
        l = 0
        r= len(height)-1
        l_max = height[l]
        r_max = height[r]
        maxWater = 0
        while l < r:
            if l_max < r_max:
                l+=1
                l_max = max(l_max,height[l])
                maxWater+= l_max - height[l]
            else:
                r -=1
                r_max = max(r_max,height[r])
                maxWater += r_max - height[r]
        return maxWater

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        
        #if h is more than len of piles we use binary search to find the value
        l,r = 1, max(piles)
        res = r

        while l<=r:
            k = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours<= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1
            

        
        return res

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        output = 0
        left, right = 0,1
        while right <= len(prices)-1:
            if prices[right] > prices[left]:
                output = max(prices[right]-prices[left], output)
            else: #means our right price is less than left price
                left = right
            right+=1
        
        return output

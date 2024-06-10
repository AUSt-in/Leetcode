class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #1. using a set to store numbers
        #2. running a while loop till we get one
        #3. converting the digits to single character
        #4. and summing up and if in set return false
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
         
        return True

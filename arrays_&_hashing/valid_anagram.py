class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        array1 = [0] * 26
        array2 = [0] * 26
        for char in s:
            array1[ord(char) - ord('a')] += 1

        
        for char in t:
            array2[ord(char) - ord('a')] += 1
        
        for i in range(26):  
            if array1[i] != array2[i]:
                return False
        
        return True
        
        
        

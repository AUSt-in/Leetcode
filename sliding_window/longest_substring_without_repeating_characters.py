
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        i,j = 0,0
        maxcount = 0
        char_set = set()
        while j< len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j+=1
                maxcount = max(maxcount, j - i)
            else: 
                char_set.remove(s[i])
                i += 1
        
        return maxcount
            

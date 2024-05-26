import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        i=0
        j=len(string)-1
        while(i<=j):
            if(string[i]!=string[j]):
                return False
            i+=1
            j-=1
        
        return True
        

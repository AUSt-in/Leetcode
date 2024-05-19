class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mappings = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mappings:
                if not stack or stack.pop() != mappings[char]: #first one checks for empty stack
                    return False

            else:
                stack.append(char)
            
        return not stack

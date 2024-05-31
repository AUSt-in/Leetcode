class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        # Initialize a hashmap to store character frequencies
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        # Initialize window start and end pointers
        window_start = 0
        window_end = 0
        # Initialize count of characters matched so far
        matched = 0

        while window_end < len(s2):
            # Expand the window by moving the end pointer
            if s2[window_end] in s1_count:
                s1_count[s2[window_end]] -= 1
                if s1_count[s2[window_end]] == 0:
                    matched += 1
            window_end += 1

            # If all characters in s1 are found in the current window, return True
            if matched == len(s1_count):
                return True

            # Shrink the window by moving the start pointer
            if window_end - window_start >= len(s1):
                if s2[window_start] in s1_count:
                    if s1_count[s2[window_start]] == 0:
                        matched -= 1
                    s1_count[s2[window_start]] += 1
                window_start += 1

        # If no match is found, return False
        return False

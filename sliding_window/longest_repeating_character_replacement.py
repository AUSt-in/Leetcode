def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # using hashmap to keep a count of movement and max character
        char_count = defaultdict(int)
        max_len = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])

            if (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len


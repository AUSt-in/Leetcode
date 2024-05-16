class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}

        for word in strs:
            word_key = ''.join(sorted(word))
            
            if word_key in anagram_groups:
                anagram_groups[word_key].append(word)
            else:
                anagram_groups[word_key] = [word]

        result = list(anagram_groups.values())
        return result

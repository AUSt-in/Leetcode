class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #using hashmap to map number to entries
        entries = {}
        #iterating through nums to map the values
        for num in nums:
            if num in entries:
                entries[num] += 1
            else:
                entries[num] =1
                
            
        #sorting hashmap according to values in descending order
        sorted_entries = sorted(entries.items(), key=lambda x: x[1], reverse=True)
        #returning a list of top two elements
        return [entry[0] for entry in sorted_entries[:k]]

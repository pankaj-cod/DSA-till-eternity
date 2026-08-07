class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        sorted_keys = sorted(freq.keys(),key=lambda x:freq[x],reverse=True)
        return sorted_keys[:k]

        
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num%2==0:
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1
        values = freq.values()
        if len(values)>0:
            mex = max(values)
        if len(freq.keys())==0:
            return -1
        for key in sorted(freq.keys()):
            if freq[key]==mex:
                return key
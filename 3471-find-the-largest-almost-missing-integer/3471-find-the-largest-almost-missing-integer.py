from collections import Counter
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0 
        right = k
        n = len(nums)
        ans = float('inf')
        freqs = {}
        for num in nums:
            freqs[num]=0

        while right<=n:
            arr = nums[left:right]
            for i in set(arr):
                freqs[i]+=1
            left+=1
            right+=1
        keys = list(freqs.keys())
        keys.sort(key = lambda x:freqs[x])
        if len(set(nums))==1 and k==1:
            return -1
        ans = -1
        for key in keys:
            if freqs[key]==1:
                ans = max(ans,key)
        return ans




            
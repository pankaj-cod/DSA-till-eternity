class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = float('inf')
        n = len(nums)
        premax = [0]*n
        suffmin = [0]*n
        premax[0]=nums[0]
        for i in range(1,n):
            premax[i]=max(premax[i-1],nums[i])
        suffmin[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffmin[i]=min(suffmin[i+1],nums[i])

        for j in range(n):
            if premax[j]-suffmin[j]<=k:
                return j
        return -1
        
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        freq = {}
        ans = -1
        for right in range(n):
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1

            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans
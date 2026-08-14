class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        ans = 0
        for right in range(len(nums)):
            
            if nums[right]!=1:
                left=right+1
            else:
                ans = max(right-left+1,ans)
        return ans
        
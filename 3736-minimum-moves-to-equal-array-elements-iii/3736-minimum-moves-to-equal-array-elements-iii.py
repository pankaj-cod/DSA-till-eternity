class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0 
        mex = max(nums)

        for i in nums:
            ans+=mex-i
        return ans
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # median would be the best choice
        # brute force
        # for optimised approach instead of increasing n-1 eles in every step we decrease max in evry step
        # make every ele equal to min
        ans = 0 
        mini = min(nums)
        for i in range(len(nums)):
            ans+=nums[i]-mini
        return ans
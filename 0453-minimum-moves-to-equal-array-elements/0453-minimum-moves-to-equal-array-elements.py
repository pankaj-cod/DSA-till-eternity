class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # median would be the best choice
        # brute force
        # for optimised approach instead of increasing n-1 eles in every step we decrease max in evry step
        # make every ele equal to min
        # its the same shi as increasing n-1 in every step but we have optimised now instead
        ans = 0 
        mini = min(nums)
        # for i in range(len(nums)):
        #     ans+=nums[i]-mini
        # return ans

        # when we open up the loop above it appearently becomes the below formula

        return sum(nums)-len(nums)*mini
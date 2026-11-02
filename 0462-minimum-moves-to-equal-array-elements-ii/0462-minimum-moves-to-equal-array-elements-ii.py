import statistics
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        median = statistics.median(nums)

        ans = 0 

        for i in nums:
            ans+=abs(i-median)
        return int(ans)
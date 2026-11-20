class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j-i+1>=l and j-i+1<=r:
                    if sum(nums[i:j+1])>0:
                        ans = min(ans,sum(nums[i:j+1]))
        
        if ans==float('inf'):
            return -1
        return ans
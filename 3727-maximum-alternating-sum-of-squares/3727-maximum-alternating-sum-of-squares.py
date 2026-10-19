class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0]*n
        odd,even = 0,0
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = nums[i]*-1
        dum = sorted(nums)
        ans = 0
        for j in range(n//2,n):
            ans+=dum[j]**2
        for k in range(n//2):
            ans-=dum[k]**2
        return ans
    
            



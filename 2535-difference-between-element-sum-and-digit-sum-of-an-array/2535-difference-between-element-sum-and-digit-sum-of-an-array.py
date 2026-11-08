class Solution:
    def differenceOfSum(self, nums: list[int]) -> int: 
        def digSum(x):
            ans = 0 
            while x>0:
                ans+=x%10
                x//=10
            return ans
        s1 = sum(nums)
        s2 = 0
        for i in nums:
            s2+=digSum(i)
        return abs(s1-s2)
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [0]*len(nums)

        for i in range(2*len(nums)-1,-1,-1):
            idx=i%len(nums)
            while(len(stack)!=0 and stack[-1]<=nums[idx]):
                stack.pop()

            if i<len(nums):
                if not stack:
                    ans[idx]=-1
                else:
                    ans[idx]=stack[-1]
            stack.append(nums[idx])

        return ans
        
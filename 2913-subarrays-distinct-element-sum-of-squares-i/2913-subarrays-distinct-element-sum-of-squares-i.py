class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = []
        fin = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                ans.append(nums[i:j+1])

        for sub in ans:
            fin+=(len(set(sub)))**2

        return fin
        # return fin
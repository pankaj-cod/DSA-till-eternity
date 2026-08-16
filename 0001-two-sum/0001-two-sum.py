class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        n = len(nums)
        ans = []
        for i in range(n):
            needed = target - nums[i]

            if needed in seen:
                ans.append(i)
                ans.append(seen[needed])
                return ans
           
            seen[nums[i]]=i
        


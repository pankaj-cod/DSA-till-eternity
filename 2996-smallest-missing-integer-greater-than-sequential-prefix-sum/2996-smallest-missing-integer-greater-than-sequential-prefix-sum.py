class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        prefix_sum = nums[0]


        for i in range(1,n):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum+=nums[i]
            else:
                break

        s = set(nums)

        ans = prefix_sum 
        while ans in s: # since we need to return the smallest number greater than equal to the sum of longest sequential prefix so we add 1 for every ans id it is in s 
            ans+=1
        
        return ans
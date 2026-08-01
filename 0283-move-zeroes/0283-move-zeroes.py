class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i,j=0,0

        while i<n:
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
            i+=1
        return nums
        
                

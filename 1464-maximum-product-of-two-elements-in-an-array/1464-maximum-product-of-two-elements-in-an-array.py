class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # product of i-1 and j-1 should be max so we can't choose last two of the sorted array
        # so we would sort the array and choose n-1 and n-2

        n = len(nums)
        nums.sort()
        i,j = n-1,n-2

        return (nums[i]-1)*(nums[j]-1)
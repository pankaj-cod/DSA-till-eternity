class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # An element which is strictly greater than its neigbours
        #Pahado wala question hoga solve
        n = len(nums)
        left = 0
        right = n-1

        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right = mid #not mid-1 becoz mid can also be the peak
        
        return left


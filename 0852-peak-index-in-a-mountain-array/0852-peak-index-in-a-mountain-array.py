class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left,right = 0,n-1

        while left<right:
            mid = (left+right)//2

            if arr[mid+1]>arr[mid]:
                left = mid+1
            else:
                right = mid
        
        return left
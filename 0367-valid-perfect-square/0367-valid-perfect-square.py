class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left,right = 1,num
        if num==1:
            return True
        while left<right:
            mid = (left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                right = mid
            else:
                left = mid+1
        
        return False
        

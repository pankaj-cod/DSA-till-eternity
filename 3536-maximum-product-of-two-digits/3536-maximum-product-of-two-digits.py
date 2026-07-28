class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        arr = []
        for i in s:
            arr.append(int(i))
        arr.sort()
        return arr[-1]*arr[-2]
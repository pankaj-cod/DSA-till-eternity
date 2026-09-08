class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(n):
            if len(str(n))<4:
                return 0
            else:
                if len(str(n))==4:
                    return 1
                if len(str(n))==5:
                    return 1
                if len(str(n))==6:
                    return 1
        count = 0
        for i in range(1,n+1):
            count+=helper(i)
        return count
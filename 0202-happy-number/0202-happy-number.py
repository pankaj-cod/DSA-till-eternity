class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            new = 0
            while n>0:
                new+=(n%10)**2
                n//=10
            
            n = new

        return True

        # new = 0
        # while new!=1:
        #     if new ==1:
        #         return True
        #     while n>0:
        #         new+=(n%10)**2
        #         n//=10
        #     n = new

        # return False
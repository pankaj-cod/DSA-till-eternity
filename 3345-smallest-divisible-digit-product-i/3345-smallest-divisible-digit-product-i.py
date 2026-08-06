class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def prod(n):
            ans = 1
            while n>0:
                ans*=n%10
                n = n//10
            return ans
        if t == 1:
            return n
        if n==1:
            return t
        elif t==2:
            for i in range(n,10*n):
                if prod(i)%2==0:
                    return i
        elif t==3:
            for i in range(n,10*n):
                if prod(i)%3==0:
                    return i
        elif t==4:
            for i in range(n,10*n):
                if prod(i)%4==0:
                    return i
        elif t==5:
            for i in range(n,10*n):
                if prod(i)%5==0:
                    return i
        elif t==6:
            for i in range(n,10*n):
                if prod(i)%6==0:
                    return i
        elif t==7:
            for i in range(n,10*n):
                if prod(i)%7==0:
                    return i
        elif t==8:
            for i in range(n,10*n):
                if prod(i)%8==0:
                    return i
        elif t==9:
            for i in range(n,10*n):
                if prod(i)%9==0:
                    return i
        elif t==10:
            for i in range(n,10*n):
                if prod(i)%10==0:
                    return i
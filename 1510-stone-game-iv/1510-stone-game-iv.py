class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [0]*(n+1)
        dp[0]=0

        for i in range(1,n+1):
            dp[i]=0
            for j in range(1,int(math.sqrt(i))+1):
                    if dp[i-j*j]==0:
                        dp[i]=1
                        break
        
        if dp[n]==1:
            return True
        return False
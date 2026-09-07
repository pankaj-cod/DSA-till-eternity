class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Duplicate subsequences generate hi na hon.Ye optimization ka important idea hai.

        n = len(s)
        dp = [0]*(n+1)
        dp[0]=1
        last = {}
        MOD = 10**9 + 7
        for i in range(1,n+1):
            ch = s[i-1]

            dp[i]=2*dp[i-1]

            if ch in last:
                dp[i]-=dp[last[ch]-1]
            
            last[ch]=i
        
        return (dp[n]-1)%MOD

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #brute force is generate all the subsequences of s and check for t in them then ans 
        # complexity will be 2^1000

        # ans = []
        # n = len(s)
        # count = 0
        # def helper(i,sub):
        #     if i>=n:
        #         ans.append(sub)
        #         return 
        #     helper(i+1,sub+s[i])
        #     helper(i+1,sub)
        # helper(0,'')
        # for i in ans:
        #     if i==t:
        #         count+=1
        # return count
        # Better brute force 
        # we traverse both with i and j we either choose from s or not 
        memo = {}
        def helper(i,j):
            if j==len(t):
                return 1
            if i ==len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==t[j]:
                memo[(i,j)]=helper(i+1,j+1)+helper(i+1,j) # here we are counting all cases if we choose i+1 or not 
            else:
                memo[(i,j)]=helper(i+1,j)
            return memo[(i,j)] # here only not choosing s[i] wale cases
        return helper(0,0)
    

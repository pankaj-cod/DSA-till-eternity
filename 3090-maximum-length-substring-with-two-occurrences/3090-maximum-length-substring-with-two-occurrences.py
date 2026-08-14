class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        n = len(s)
        left = 0
        ans = 0 
        for right in range(n):
            if s[right] in freq:
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            
            while freq[s[right]]>2:
                freq[s[left]]-=1
                left+=1
            
            ans = max(ans,right-left+1)
        return ans
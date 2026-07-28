class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Since the string is already palindromic so we have to get the lexicographically smallest first half of the string then the other half will be its reverse
        n = len(s)
        if n==1:
            return s
        if n%2==0:
            arr = sorted(s[:n//2])
            half = "".join(arr)
            nxt = half[::-1]
            ans = half+nxt
            return ans
        else:
            arr = sorted(s[:n//2])
            half = "".join(arr)
            nxt = half[::-1]
            half+=s[n//2]
            ans = half+nxt
            return ans






class Solution:
    def countAndSay(self, n: int) -> str:

        if n==1:
            return '1'
        
        s = self.countAndSay(n-1)
        ans = ""
        i = 0

        while i < len(s):
            count = 0
            ch = s[i]

            while i<len(s) and s[i]==ch:
                count +=1
                i += 1
            
            ans += str(count) + ch
        
        return ans

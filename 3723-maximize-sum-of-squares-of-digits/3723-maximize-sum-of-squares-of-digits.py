class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ''
        if sum>9*num:
            return ""
        if sum>9:
            while sum>9:
                ans+=str(9)
                num-=1
                sum-=9
            else:
                ans+=str(sum)
                num-=1
            while num>0:
                ans+='0'
                num-=1
        
        else:
            ans = str(sum)
            while num-1>0:
                ans+='0'
                num-=1
        
        return ans
            
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        
        def selfdiv(x):
            s = str(x)
            for i in s:
                if i!='0':
                    if x%int(i)!=0:
                        return False
                else:
                    return False
            return True
        ans = []
        for num in range(left,right+1):
            if selfdiv(num)==True:
                ans.append(num)
        
        return ans
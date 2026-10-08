class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = []
        for i in s:
            if i=="(":
                if count!=0:
                    result.append(i)
                count+=1
            else:
                count-=1
                if count!=0:
                    result.append(i)
        
        return "".join(result)
            

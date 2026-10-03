class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack)>=3 and stack[-1]=='c' and stack[-2]=='b' and stack[-3]=='a':
                stack.pop()
                stack.pop()
                stack.pop()
            
        if len(stack)==0:
            return True
        return False
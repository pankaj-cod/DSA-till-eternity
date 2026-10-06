class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i=="(":
                stack.append(")")

            elif len(stack)>0 and i==")":
                stack.pop()
            else:
                ans+=1 # i cant push ")" to stack coz it would be popped by a later "(" now i get it
        return ans+len(stack)
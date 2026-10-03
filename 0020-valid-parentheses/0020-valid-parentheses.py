class Solution:
    def isValid(self, s: str) -> bool:
        # the idea is we trav the string and everytime we see an opening bracket we add a closing bracket to the stack 
        # if i encounter an opening one i append the closing on the stack
        stack = []
        if len(s)==1:
            return False

        for i in s:
            if i =="(":
                stack.append(")")
            elif i=="{":
                stack.append("}")
            elif i=="[":
                stack.append("]")
            elif stack==[] or stack.pop()!=i:
                return False
        
        if len(stack)==0:
            return True
        return False
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in s:
            if i=="(":
                stack.append(0) # appending 0 coz we are creating new level evrytime we see "("
            elif i ==")":#we dont add it to ans as the parent grp could still contribute 
                score = stack.pop()
                if score==0:
                    score=1
                else:
                    score*=2
                stack[-1]+=score
        
        return stack[0]
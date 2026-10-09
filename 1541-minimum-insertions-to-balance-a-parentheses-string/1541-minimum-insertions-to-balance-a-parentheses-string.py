class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        n = len(s)
        ans = 0
        i = 0

        while i < n:
            if s[i] == "(":
                stack.append("(")
                i += 1

            else:
                if i + 1 < n and s[i + 1] == ")":
                    i += 2
                else:
                    ans += 1
                    i += 1

                if stack:
                    stack.pop()
                else:
                    ans += 1

        return 2 * len(stack) + ans


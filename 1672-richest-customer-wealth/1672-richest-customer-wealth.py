class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = -1*float('inf')

        for i in accounts:
            ans = max(ans,sum(i))
        
        return ans
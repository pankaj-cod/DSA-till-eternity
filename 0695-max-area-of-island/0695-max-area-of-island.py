class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans = -float('inf')
        if not grid:
            return
        n = len(grid)
        m = len(grid[0])
        def dfs(r,c,s):
            if (r<0 or r>=n) or (c<0 or c>=m) or grid[r][c]==0:
                return 
            
            s.append(grid[r][c])
            grid[r][c] = 0 

            dfs(r-1,c,s)
            dfs(r+1,c,s)
            dfs(r,c-1,s)
            dfs(r,c+1,s)


        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    s = []
                    dfs(i,j,s)
                    ans = max(ans,sum(s))

        if ans==-float('inf'):
            return 0  
        return ans
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        arr = []
        count = 0 
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        islands = 0 
        s = 0
        def dfs(r,c,lst):
            if (r<0 or r>=rows) or (c<0 or c>=cols) or grid[r][c]==0:
                return 
            # marking visited
            lst.append(grid[r][c]) 
            grid[r][c] = 0

            dfs(r+1,c,lst)
            dfs(r-1,c,lst)
            dfs(r,c+1,lst)
            dfs(r,c-1,lst)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] !=0:
                    islands += 1
                    lst = []
                    dfs(r, c,lst)
                    arr.append(lst)

        for island in arr:
            if sum(island)%k==0:
                count+=1
        
        return count
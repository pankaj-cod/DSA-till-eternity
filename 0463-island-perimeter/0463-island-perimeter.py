class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        count = 0

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 4

                    if i > 0 and grid[i-1][j] == 1:
                        count -= 2

                    if j > 0 and grid[i][j-1] == 1:
                        count -= 2

        return count
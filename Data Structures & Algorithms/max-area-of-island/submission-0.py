class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxx = 0
        
        def ff(x, y, grid):
            if (x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0):
                return 0
            
            if grid[x][y] == 1:
                grid[x][y] = 0

            return 1 + ff(x+1, y, grid) + ff(x, y+1, grid) + ff(x-1, y, grid) + ff(x, y-1, grid)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = ff(i, j, grid)
                    if temp > maxx:
                        maxx = temp

                    

        return maxx
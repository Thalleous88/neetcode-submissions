class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def ff(x, y):
            nonlocal count
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0 or grid[x][y] == -1:
                return count

            
            grid[x][y] = -1

            temp = 4
            if x-1 >= 0 and (grid[x-1][y] == 1 or grid[x-1][y] == -1):
                temp -= 1
            
            if x+1 < row and (grid[x+1][y] == 1 or grid[x+1][y] == -1):
                temp -= 1

            if y-1 >= 0 and (grid[x][y-1] == 1 or grid[x][y-1] == -1):
                temp -= 1

            if y+1 < col and (grid[x][y+1] == 1 or grid[x][y+1] == -1):
                temp -= 1

            count += temp

            ff(x+1, y)
            ff(x, y-1)
            ff(x, y+1)
            ff(x-1, y)

            return count

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count = 0
                    return ff(i, j)

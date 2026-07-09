class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        

        
        count = 0
        row, col = len(grid), len(grid[0])


       
        def ff(x, y, grid):
            if (x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == '0'):
                return
            
            if grid[x][y] == '1':
                grid[x][y] = '0'

            ff(x+1, y, grid)
            ff(x, y+1, grid)
            ff(x-1, y, grid)
            ff(x, y-1, grid)

            

            




        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    ff(i, j, grid)
                

        return count



class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(x, y):
            if x < 0 or x >= row or y >= col or y < 0 or (x, y) in visit or grid[x][y] == -1:
                return
            
            q.append([x, y])
            visit.add((x, y))

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    q.append([x, y])
                    visit.add((x, y))

        dist = 0

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = dist

                addRoom(x+1, y)
                addRoom(x, y+1)
                addRoom(x-1, y)
                addRoom(x, y-1)

            dist += 1


    

                
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        visited = [[0 for i in range(col)] for _ in range(row)]
        total = row * col

        x, y = 0, 0
        state = 0
        res = []
        while len(res) < total:
            if x < 0 or x >= row or y < 0 or y >= col or visited[x][y] == 1:
                if state == 0:
                    y -= 1
                elif state == 1:
                    x -= 1
                elif state == 2:
                    y += 1
                elif state == 3:
                    x += 1
                
                state = ((state + 1) % 4)
            else:
                visited[x][y] = 1
                res.append(matrix[x][y])

            if state == 0:
                y += 1
            elif state == 1:
                x += 1
            elif state == 2:
                y -= 1
            elif state == 3:
                x -= 1

        return res

        
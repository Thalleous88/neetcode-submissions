import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        row, col = len(board), len(board[0])

        def dfs(x, y, windex, word, new):
            if x < 0 or x >= row or y < 0 or y >= col or new[x][y] == -1 or windex >= len(word) or word[windex] != new[x][y]:
                return False

            if windex == len(word) - 1 and word[windex] == new[x][y]:
                return True


            if word[windex] == new[x][y]:
                temp = new[x][y]
                new[x][y] = -1
                find = dfs(x+1, y, windex+1, word, new) or dfs(x, y+1, windex+1, word, new) or dfs(x-1, y, windex+1, word, new) or dfs(x, y-1, windex+1, word, new)

                new[x][y] = temp
                return find


        

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    
                    if len(word) == 1:
                        return True
                    
                    if dfs(i, j, 0, word, board):
                        return True

        return False

        


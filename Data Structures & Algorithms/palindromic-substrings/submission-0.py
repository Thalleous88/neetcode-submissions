class Solution:
    def countSubstrings(self, s: str) -> int:
        s = list(s)
        l = len(s)

        count = 0
        memo = [[None for _ in range(l)] for _ in range(l)]
        def dp(x, y):
            if x >= y:
                return True

            if memo[x][y] is not None:
                return memo[x][y]
            
            memo[x][y] = (s[x] == s[y] and dp(x+1, y-1))

            return memo[x][y] 

        for x in range(l):
            for y in range(x, l):
                if dp(x, y):
                    count += 1

        return count
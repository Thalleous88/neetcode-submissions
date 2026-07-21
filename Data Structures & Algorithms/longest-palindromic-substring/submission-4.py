class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        s = list(s)

        l = len(s)

        best = ""

        memo = [[None for _ in range(l)] for _ in range(l)]

        def dp(x, y):
            if x >= y:
                return True

            if memo[x][y]:
                return memo[x][y]
            
            memo[x][y] = (s[x] == s[y] and dp(x+1, y-1))

            return memo[x][y]

        for x in range(len(s)):
            for y in range(len(s)):
                if dp(x, y):
                    if y-x+1 > len(best):
                        best = s[x:y+1]

        return "".join(best)




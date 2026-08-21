class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        i = 0
        res = ""

        while True:
            if i >= len(word1) and i >= len(word2):
                return res
            elif i >= len(word1):
                res += word2[i]
            elif i >= len(word2):
                res += word1[i]
            else: 
                res += word1[i]
                res += word2[i]

            i += 1

        return res
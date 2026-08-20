class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""

        shortest = min(strs, key=len)
        length = len(shortest)

        loop = True
        i = 0
        while i < len(shortest) and loop:
            temp = ""
            for st in strs:
                if temp == "":
                    temp += st[i]
                elif temp != st[i]:
                    loop = False
                    return lcp

            i += 1
            
            lcp += temp

        return lcp
                
                

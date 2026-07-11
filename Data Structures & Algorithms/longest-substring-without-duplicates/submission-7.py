class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        x = 0
        y = 0

        best = 0
        temp = []
        
        while y < len(s) and x < len(s):
      
            if s[y] not in temp:
                temp.append(s[y])
                y += 1
            else:
                curr = len(temp)
             
                if curr > best:
                    best = curr
                    

                x += 1
                y = x
                temp.clear()

        if len(temp) > best:
            best = len(temp)
     
        return best

        
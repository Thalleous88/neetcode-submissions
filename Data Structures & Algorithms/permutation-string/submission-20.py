class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)

        dct = defaultdict(int)

        for char in s1:
            dct[char] += 1
        
        print(dct)

        if len(s1) > len(s2):
            return False

        x = 0
        y = 0
        ans = defaultdict(int)
        while x < len(s2) and y <= len(s2):
            # if y < len(s2):
            #     print(ans)
            if ans == dct:
                print(ans)
                return True

            if y < len(s2) and s2[y] in ans and ans[s2[y]] + 1 > dct[s2[y]]:
                if s2[x] in ans:
                    ans[s2[x]] -= 1
                if ans[s2[x]] == 0:
                    ans.pop(s2[x])

                x += 1
            elif y < len(s2) and s2[y] in dct:
                ans[s2[y]] += 1
                y += 1
            else:
                x += 1
                y = x
                ans.clear()
                
               

        return False

               
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        check = {}
        true = {}

        
        state = 0
        
        if len(s) < len(t):
            return ""
        if sorted(s) == sorted(t):
            return "".join(s)

        tot = 0
        for char in t:
            if char not in true:
                true[char] = 0

            true[char] += 1
            tot += 1

        print(true)

        x = 0
        y = 0
        currbest = [0 for _ in range(len(s))]
        test = currbest.copy()
        curr = []
        while x <= len(s) and y <= len(s):
            print(check)
            if true.keys() == check.keys() and all(check[k] >= true[k] for k in true.keys()) and len(curr) <= len(currbest):
                currbest = list(curr)
                x += 1
                y = x
                state = 0
                curr.clear()
                check.clear()
            elif y < len(s) and s[y] in t:
                if s[y] not in check:
                    check[s[y]] = 0
                
                check[s[y]] += 1
                curr.append(s[y])
                
                y += 1
                state = 1

                
            elif y < len(s) and state and sum(check.values()) != len(t):
                curr.append(s[y])
                y += 1
            else:
                x += 1
                y = x
                state = 0
                curr.clear()
                check.clear()

        if test == currbest:
            return ""

        res = "".join(currbest)

        return res
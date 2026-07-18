class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 1
        l = len(digits)-1
        for digit in digits:
            res += (digit * (10**l))
            l -= 1

        lst = []
        res = str(res)
        res = list(res)

        for r in res:
            lst.append(r)

        return lst
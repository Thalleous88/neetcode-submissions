class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        res = []

        def bisearch(h, piles, left, right):
            if (right >= left):
                mid = left + (right-left) // 2
                tes = [pile // mid if (pile / mid == pile // mid) else (pile // mid) + 1  for pile in piles]
                tes = sum(tes)

                print(tes)

                if tes <= h:
                    res.append(mid)
                    return bisearch(h, piles, left, mid-1)
                else:
                    return bisearch(h, piles, mid+1, right)
            else:
                return
        
        t = bisearch(h, piles, 1, max(piles))
        print(res)
        res = min(res)
      
        return res

        
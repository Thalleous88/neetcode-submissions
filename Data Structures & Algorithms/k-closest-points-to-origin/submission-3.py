import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            prio = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(pq, (prio, point))

        res = []

        for i in range(k):
            res.append(pq[0][1])
            heapq.heappop(pq)

        
        return res
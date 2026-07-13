class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        temp = 0
        while len(stones) > 1:
            print(stones)
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            res = abs(stone1 - stone2)

            if res == 0:
                continue
            
            heapq.heappush(stones, -1 * res)

            


        if len(stones) == 0:
            return 0
        
        return -1 * heapq.heappop(stones)
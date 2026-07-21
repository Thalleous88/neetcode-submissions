class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        lst = []
        for i in range(len(gas)):
            lst.append(gas[i] - cost[i])

        total = 0
        res = 0
        if sum(lst) < 0:
            return -1

        for i in range(len(lst)):
            total += lst[i]
            
            if total < 0:
                res = i+1
                total = 0

        return res
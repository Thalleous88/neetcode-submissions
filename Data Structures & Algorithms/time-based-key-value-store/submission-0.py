class TimeMap:

    def __init__(self):
        self.ht = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ht[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.ht[key]) - 1

        temp, res = float('inf'), ""

        while left <= right:
            mid = (left + right) // 2

            check = timestamp - self.ht[key][mid][0]
            if check > 0 and check < temp:
                temp = timestamp - self.ht[key][mid][0]
                res =  self.ht[key][mid][1]

            if self.ht[key][mid][0] == timestamp:
                return self.ht[key][mid][1]

            elif self.ht[key][mid][0] > timestamp:
                right = mid-1
            else:
                left = mid+1
                

        return res
        

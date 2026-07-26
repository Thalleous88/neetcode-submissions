class TimeMap:

    def __init__(self):
        self.ht = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ht[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.ht[key]) - 1

        res = ""

        while left <= right:
            mid = (left + right) // 2
            if self.ht[key][mid][0] <= timestamp:
                res = self.ht[key][mid][1]
                left = mid+1

            else:
                right = mid-1
           
                
                

        return res
        

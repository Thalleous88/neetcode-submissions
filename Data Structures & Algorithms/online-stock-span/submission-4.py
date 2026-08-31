class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        queue = deque()
        while self.stack and self.stack[-1] <= price:
            queue.append(self.stack.pop())
            count += 1

        while queue:
            self.stack.append(queue.popleft())

        self.stack.append(price)

        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
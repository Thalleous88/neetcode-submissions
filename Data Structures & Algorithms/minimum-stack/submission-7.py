class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.queue = deque()

    
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

        if not self.queue or self.queue[0] < val:
            self.queue.appendleft(val)

    def pop(self) -> None:
        num = self.stack.pop()

        if self.minstack and self.minstack[-1] == num:
            self.minstack.pop()

        if self.queue and self.queue[0] == num:
            self.queue.popleft()
        

    def top(self) -> int:
        return self.stack[-1]
        
        
    def getMin(self) -> int:
        if not self.minstack:
            return self.queue[0]

        if not self.queue:
            return self.minstack[-1]

        if self.minstack[-1] < self.queue[0]:
            return self.minstack[-1]
        else:
            return self.queue[0]
        

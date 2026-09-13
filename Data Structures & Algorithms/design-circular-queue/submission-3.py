class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.capacity = 0

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.k:
            return False
        
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            node = ListNode(value)
            self.tail.next = node
            self.head.prev = node
            node.next = self.head
            node.prev = self.tail
            self.tail = node

        self.capacity += 1
        return True
        

    def deQueue(self) -> bool:
        if self.capacity == 0:
            return False

        if self.capacity == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail

        self.capacity -= 1
        return True

    def Front(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        if self.capacity == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.capacity == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = ListNode(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        
        self.tail.next = new_node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        if self.cache[key].next is None:
            return self.cache[key].value

        if self.cache[key].prev is None:
            self.linked_list.head = self.linked_list.head.next
            self.linked_list.head.prev = None
            self.cache[key].next = None
            self.linked_list.tail.next = self.cache[key]
            self.linked_list.tail.next.prev = self.linked_list.tail
            self.linked_list.tail = self.linked_list.tail.next

            return self.cache[key].value
        
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev

        self.cache[key].prev = self.linked_list.tail
        self.linked_list.tail.next = self.cache[key]
        self.linked_list.tail = self.linked_list.tail.next
        self.cache[key].next = None

        return self.cache[key].value
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.linked_list.append(key, value)
            self.cache[key] = self.linked_list.tail

        if len(self.cache) > self.capacity:
            k = self.linked_list.head.key
            self.linked_list.head = self.linked_list.head.next
            self.cache.pop(k)

            if self.linked_list.head:
                self.linked_list.head.prev = None
            else:
                self.linked_list.tail = None

            return

        self.cache[key].value = value
        if self.cache[key].next is None:
            return

        if self.cache[key].prev is None:
            self.linked_list.head = self.linked_list.head.next
            self.linked_list.head.prev = None
            self.cache[key].next = None
            self.linked_list.tail.next = self.cache[key]
            self.linked_list.tail.next.prev = self.linked_list.tail
            self.linked_list.tail = self.linked_list.tail.next

            return 
        
        
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev
        self.cache[key].next = None

        self.cache[key].prev = self.linked_list.tail
        self.linked_list.tail.next = self.cache[key]
        self.linked_list.tail = self.linked_list.tail.next
        self.cache[key].next = None

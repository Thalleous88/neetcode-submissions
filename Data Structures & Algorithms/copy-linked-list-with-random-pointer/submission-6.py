"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        hash_table = {}

        while head:
            hash_table[head] = Node(head.val)
            head = head.next

        for node in hash_table.keys():
            hash_table[node].val = node.val
            if node.next is None:
                hash_table[node].next = None
            else:
                hash_table[node].next = hash_table[node.next]
            if node.random is None:
                hash_table[node].random = None
            else:
                hash_table[node].random = hash_table[node.random]


        return hash_table[curr]

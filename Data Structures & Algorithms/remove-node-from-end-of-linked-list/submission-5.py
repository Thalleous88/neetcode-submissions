# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr != None:
            curr = curr.next
            l += 1
        
        if l == 1:
            head = None
            return 

        if l == n:
            head = head.next
            return head

        if l == 2:
            head.next = None
            
            return head

        

        count = 0
        curr2 = head
        while curr2.next != None and count != (l - n - 1):
            curr2 = curr2.next
            count += 1

        print(count)

        temp = curr2.next
        print(curr2.val)
        curr2.next = temp.next
        temp.next = None

        return head

        

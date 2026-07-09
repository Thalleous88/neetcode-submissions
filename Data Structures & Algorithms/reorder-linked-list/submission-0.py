# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

     

        
        while curr.next != None and curr.next.next != None:
            temp = curr
            temp2 = None
            while temp.next != None:
                temp2 = temp
                temp = temp.next
            temp3 = curr.next

            curr.next = temp
            curr = curr.next
            temp2.next = None
            curr.next = temp3
            curr = curr.next
        
        
            
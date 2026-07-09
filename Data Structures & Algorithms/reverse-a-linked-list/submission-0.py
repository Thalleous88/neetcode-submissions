# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []

        if head is None:
            return head

        temp = head
        while (temp != None):
            arr.append(temp.val)
            temp = temp.next

        l = len(arr)-1

        res = ListNode(val=arr[l])

        t = res

        l -= 1

        while l >= 0:
            t.next = ListNode(val=arr[l])
            t = t.next
            l -= 1

        return res

        
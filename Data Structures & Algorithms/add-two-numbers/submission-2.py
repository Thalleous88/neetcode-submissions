# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        curr2 = l2

        linked_list = ListNode()
        head = linked_list

        

        temp = 0
        while curr and curr2:
            tot = curr.val + curr2.val + temp
            temp = 0
            if tot > 9:
                tot -= 10
                temp = 1


            linked_list.val = tot
            if curr.next or curr2.next:
                linked_list.next = ListNode()
                linked_list = linked_list.next



            curr = curr.next
            curr2 = curr2.next

        while curr:
            tot = curr.val + temp
            temp = 0
            if tot > 9:
                tot -= 10
                temp = 1

            linked_list.val = tot
            if curr.next:
                linked_list.next = ListNode()
                linked_list = linked_list.next
            curr = curr.next

        while curr2:
            tot = curr2.val + temp
            temp = 0
            if tot > 9:
                tot -= 10
                temp = 1

            linked_list.val = tot
            if curr2.next: 
                linked_list.next = ListNode()
                linked_list = linked_list.next
            curr2 = curr2.next

        if temp == 1:
            linked_list.next = ListNode(val=1)

        return head

            

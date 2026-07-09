# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = list1
        if list1 is None and list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            while (list2 != None):
                val = list2.val
                while (True):
                    if list1.val <= val and list1.next is None:
                        temp = ListNode(val)
                        list1.next = temp
                        break
                    elif (list1.val <= val and list1.next.val >= val):
                        temp = ListNode(val, list1.next)
                        list1.next = temp
                        break
                    elif (list1.val > val):
                        temp = ListNode(val, list1)
                        list1 = temp
                        head = list1
                        break
                    
                    list1 = list1.next
                    
                        
                list2 = list2.next
            
            return head

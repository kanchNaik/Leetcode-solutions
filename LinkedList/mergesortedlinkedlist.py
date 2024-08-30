# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = list1
        l2 = list2
        head = ListNode()
        current = head

        while (l1 is not None or l2 is not None):
            if(l1 is not None and l2 is None):
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif(l2 is not None and l1 is None):
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif(l1.val < l2.val):
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif(l2.val < l1.val):
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif(l1.val == l2.val):
                current.next = ListNode(l1.val)
                current = current.next
                current.next = ListNode(l2.val)
                l1 = l1.next
                l2 = l2.next

            current = current.next
        return head.next
                

        
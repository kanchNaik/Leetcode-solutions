from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            val = val1 + val2 + carry
            current.next = ListNode(val % 10)
            current = current.next
            carry = val // 10
            l1 = l1.next
            l2 = l2.next

        return head.next
    
sol = Solution()
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

linknode = sol.addTwoNumbers(l1, l4)
while linknode is not None:
    print(linknode.val)
    linknode = linknode.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0
        print(l1.val)
        
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            val = val1 + val2 + carry
            print(val)
            print('Carry -', carry)
            carry = val //10
            current.next = ListNode(val % 10)
            current = current.next

            if(l1 is not None):
                l1 = l1.next
            if(l2 is not None):
                l2 = l2.next   

        
        return head.next
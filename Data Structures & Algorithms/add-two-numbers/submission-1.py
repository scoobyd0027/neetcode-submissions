# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        node1, node2 = l1, l2
        dummy = ListNode(0)
        total = dummy
        while node1 or node2 or rem:
            cur = (node1.val if node1 else 0) + (node2.val if node2 else 0) + rem
            total.next = ListNode(cur % 10)
            rem = cur // 10
            total = total.next
            if node1: node1 = node1.next
            if node2: node2 = node2.next
        
        return dummy.next

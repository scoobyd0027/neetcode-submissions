# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(node):
            if not node: return 0
            count = rec(node.next)
            if count == n:
                node.next = node.next.next
            return count + 1

        dummy = ListNode(0)
        dummy.next = head
        rec(dummy)
        return dummy.next
        

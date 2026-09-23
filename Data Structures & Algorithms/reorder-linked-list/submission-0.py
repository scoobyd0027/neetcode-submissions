# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head

            new_head = reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = head
        reverse = reverseList(slow.next)
        slow.next = None
        while node and reverse:
            node_next = node.next
            reverse_next = reverse.next
            node.next = reverse
            reverse.next = node_next
            node = node_next
            reverse = reverse_next

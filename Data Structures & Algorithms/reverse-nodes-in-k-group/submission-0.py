# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node):
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        counter = 0
        groups = []
        last_head = node
        while node:
            next = node.next
            counter += 1
            if counter % k == 0:
                groups.append(last_head)
                last_head = next
                node.next = None
            node = next

        dummy = ListNode(0)
        cur = dummy
        for group in groups:
            new_head = self.reverse(group)
            cur.next = new_head
            cur = group
        
        cur.next = last_head
        return dummy.next

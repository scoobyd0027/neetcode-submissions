# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        
        return prev

'''
0, 1, 2, 3, None

None
3 -> 2 ->
2
1 -> 0 -> None
'''
    

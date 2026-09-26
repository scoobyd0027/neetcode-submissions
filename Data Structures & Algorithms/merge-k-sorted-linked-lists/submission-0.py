# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            if node is not None:
                heapq.heappush(heap, Node(node))
        
        dummy = ListNode(0)
        node = dummy 
        while heap:
            wrap = heapq.heappop(heap)
            node.next = wrap.node
            node = node.next
            if wrap.node.next:
                heapq.heappush(heap, Node(wrap.node.next))
        
        return dummy.next

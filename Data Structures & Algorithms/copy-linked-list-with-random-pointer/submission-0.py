"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None}
        node = head
        dummy = Node(0)
        copy = dummy

        while node:
            new = Node(node.val) if node not in seen else seen[node]
            copy.next = new
            seen[node] = new
            copy = copy.next
            node = node.next

        node = head
        copy = dummy.next
        while node:
            random = seen[node.random] if node.random in seen else Node(node.random.val)
            copy.random = random
            seen[node.random] = random
            node = node.next
            copy = copy.next
            
        return dummy.next
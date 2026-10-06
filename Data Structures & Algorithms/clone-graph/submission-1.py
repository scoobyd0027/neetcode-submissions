"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, orig: Optional['Node']) -> Optional['Node']:
        if not orig: return None
        q = deque([orig])
        map = {orig: Node(orig.val)}
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in map:
                    map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                map[node].neighbors.append(map[neighbor])

        return map[orig]
                

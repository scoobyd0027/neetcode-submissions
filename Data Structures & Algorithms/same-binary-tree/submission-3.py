# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        d = deque([(p, q)])
        while d:
            p, q = d.popleft()
            if not p or not q or p.val != q.val:
                return False
            
            if p.left or q.left:
                d.append((p.left, q.left))
            
            if p.right or q.right:
                d.append((p.right, q.right))
            
        return True

            

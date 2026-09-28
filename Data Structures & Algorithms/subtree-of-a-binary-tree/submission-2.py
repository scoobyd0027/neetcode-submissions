# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, p, q):  
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


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

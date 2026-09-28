# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subRoot):  
        if not root and not subRoot: return True

        q = deque([(root, subRoot)])
        while q:
            r, s = q.popleft()
            if not r or not s or r.val != s.val:
                return False
            
            if r.left or s.left:
                q.append((r.left, s.left))
            
            if r.right or s.right:
                q.append((r.right, s.right))
        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

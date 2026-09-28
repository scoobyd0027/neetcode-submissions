# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(root, minV, maxV):
            if not root: return True
            if not (minV < root.val < maxV): return False

            left, right = not root.left, not root.right
            if root.left and root.val > root.left.val:
                left = traverse(root.left, minV, root.val)
            
            if root.right and root.val < root.right.val:
                right = traverse(root.right, root.val, maxV)
            
            return left and right
        
        return traverse(root, -sys.maxsize, sys.maxsize)
        
'''
        0
    /       \
-1000      1000
            /
           0 
'''
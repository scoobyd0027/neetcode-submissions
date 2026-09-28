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

            return traverse(root.left, minV, root.val) and traverse(root.right, root.val, maxV)
        
        return traverse(root, -sys.maxsize, sys.maxsize)
        
'''
        0
    /       \
-1000      1000
            /
           0 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def computeHeight(root):
            if not root: return 0

            left = computeHeight(root.left)
            right = computeHeight(root.right)

            if abs(left - right) > 1:
                return sys.maxsize

            return max(left, right) + 1
        
        res = computeHeight(root)
        return res < sys.maxsize 

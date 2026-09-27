# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def calculateDiameter(root):
            nonlocal maxD
            if not root: return 0
            
            left = calculateDiameter(root.left)
            right = calculateDiameter(root.right)

            maxD = max(maxD, left + right)
            return max(left, right) + 1

        calculateDiameter(root)
        return maxD


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -sys.maxsize
        def calculate(node):
            nonlocal maxSum
            if not node: return 0

            left = calculate(node.left)
            right = calculate(node.right)

            subTreeMax = max(left + node.val, right + node.val, node.val)
            maxSum = max(maxSum, left + right + node.val, subTreeMax)
            return subTreeMax

        calculate(root)
        return maxSum
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def traverse(node, maxV):
            nonlocal root
            if not node: return 0

            maxV = max(maxV, node.val)
            left = traverse(node.left, maxV)
            right = traverse(node.right, maxV)
            return left + right + int(node.val >= maxV)

        return traverse(root, -sys.maxsize)

'''
2
 \
  4
  /\
 10 8
    /
   4 
   
'''
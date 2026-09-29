# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i, j = 0, 0
        map = defaultdict(deque)
        for i, num in enumerate(inorder):
            map[num].append(i)
        
        i = 0
        def dfs(l, r):
            nonlocal map, i, preorder

            if i == len(preorder) or l > r: return None
            node = TreeNode(preorder[i])
            i += 1

            j = map[node.val].popleft()
            node.left = dfs(l, j - 1)
            node.right = dfs(j + 1, r)

            return node
        
        return dfs(0, len(inorder) - 1)



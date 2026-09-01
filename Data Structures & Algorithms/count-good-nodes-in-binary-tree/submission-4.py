# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_par):
            nonlocal count
            if not node:
                return
            if node.val >=max_par:
                count += 1
            max_par = max(max_par, node.val)
            dfs(node.left, max_par)
            dfs(node.right, max_par)
        dfs(root, float('-inf'))
        return count
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.md = 0
        def dfs(cur, deep):
            self.md = max(self.md, deep)
            if cur.left:
                dfs(cur.left, deep + 1)
            if cur.right:
                dfs(cur.right, deep + 1)
        if root:
            dfs(root, 1)
        return self.md
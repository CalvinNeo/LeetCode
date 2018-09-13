# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(l, r):
            if not l and not r:
                return True
            elif (l and not r) or (not l and r):
                return False
            else:
                if l.val == r.val:
                    return dfs(l.left, r.right) and dfs(l.right, r.left)
                else:
                    return False
        if not root:
            return True
        else:
            return dfs(root.left, root.right)
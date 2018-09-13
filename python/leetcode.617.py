# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from utils import *


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def dfs(c1, c2):
            root = None
            if c1 or c2:
                root = TreeNode(0)
            if c1:
                root.val += c1.val
            if c2:
                root.val += c2.val
            if c1 or c2:
                root.left = dfs(None if not c1 else c1.left, None if not c2 else c2.left)
                root.right = dfs(None if not c1 else c1.right, None if not c2 else c2.right)
            return root
        return dfs(t1, t2)

# sln = Solution()
# print sln.mergeTrees(make_tree([1,3,2,5]), make_tree([2,1,3,null,4,null,7]))
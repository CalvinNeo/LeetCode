# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        def dfs(cur):
            robl, norobl, robr, norobr = 0, 0, 0, 0
            if not cur.left and not cur.right:
                return cur.val, 0
            if cur.left:
                robl, norobl = dfs(cur.left)
            if cur.right:
                robr, norobr = dfs(cur.right)
            return cur.val + norobl + norobr, max(robl, norobl) + max(robr, norobr)
        return max(dfs(root))

sln = Solution()

N1 = make_tree([3,2,3,null,3,null,1])
print sln.rob(N1)

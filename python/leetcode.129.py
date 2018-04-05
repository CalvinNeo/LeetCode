# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils import *

ans = 0
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global ans
        ans = 0
        if root == None:
            return 0
        def dfs(accu, cur):
            global ans
            if not cur.left and not cur.right:
                ans += accu * 10 + cur.val
                return
            if cur.left:
                dfs(accu * 10 + cur.val, cur.left)
            if cur.right:
                dfs(accu * 10 + cur.val, cur.right)
        dfs(0, root)
        return ans

sln = Solution()
print sln.sumNumbers(TreeNode(0))
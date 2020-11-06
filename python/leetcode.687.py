# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(cur):
            l = 0
            r = 0
            if cur.left:
                if cur.left.val == cur.val:
                    l = 1 + dfs(cur.left)
                else:
                    dfs(cur.left)

            if cur.right:
                if cur.right.val == cur.val:
                    r = 1 + dfs(cur.right)
                else:
                    dfs(cur.right)

            if not cur.left and not cur.right:
                return 0
            elif cur.left and cur.right and cur.left.val == cur.val and cur.right.val == cur.val:
                self.ans = max(self.ans, l + r)
            else:
                self.ans = max(self.ans, max(l, r))
            return max(l, r)

        if not root:
            return 0
        else:
            dfs(root)
            return self.ans

sln = Solution()
print sln.longestUnivaluePath(make_tree([5,4,5,1,1,5])) # 2
print sln.longestUnivaluePath(make_tree([5,4,5])) # 1
print sln.longestUnivaluePath(make_tree([1,4,5,4,4,5])) # 2
print sln.longestUnivaluePath(make_tree([1,5,8,9,7,7,8,1,4,8,1,9,0,8,7,1,7,4,2,9,8,2,4,null,null,9,null,null,null,6,0,9,4,1,0,1,8,9,0,1,8,9,1,0,9,6,2,5,null,2,3,0,2,4,8,8,8,5,0,0,9,4,9,1,null,0,7,2,2,3,null,6,1,0,8,9,9,9,4,8,4,3,4,4,0,null,null,8,3,8,null,null,0,null,0,4,9,1,2,null,4,4,0,4,3,5,5,7,4,1,6,null,1,0,null,null,null,2,8,7,7,null,null,0,2,5,5,9,3,3,null,7,6,6,7,9,8,1,7,7,7,2,6,null,7,null,4,6,4,6,null,null,9,1,null,null,null,5,5,5,4,2,2,8,5,1,1,3,1,3,7,null,2,null,9,1,4,4,7,7,null,1,5,6,2,7,3,null,9,1,null,2,4,4,8,null,null,7,null,6,null,7,4,3,5,8,4,8,5,null,null,8,null,null,null,4,4,null,null,null,null,8,3,5,5,null,null,null,1,2,0,null,null,9,3,null,8,3,7,1,8,9,0,1,8,2,null,4,null,null,8,null,null,null,null,2,null,4,8,5,5,3,1,null,null,6,null,1,null,null,6,null,null,null,null,7,3,null,null,null,8,6,4,null,6,9,0,7,8,null,null,0,6,7,null,null,0,0,7,2,3,2,null,0,2,3,null,0,1,7,9,0,7,null,null,null,null,5,8,2,6,3,2,0,4,null,null,0,9,1,1,1,null,1,3,null,7,9,1,3,3,8,null,null,null,null,6,null,null,null,null,9,8,1,3,8,3,0,6,null,null,8,5,6,5,2,1,null,5,null,7,0,0,null,9,3,9,null,3,0,0,9,1,7,0,2,null,6,8,5,null,null,null,null,null,7,null,2,5,null,null,9,null,null,null,null,null,null,null,null,null,null,null,4,1,null,3,6,6,2,5,5,9,null,null,7,8,null,null,2,7,3,7,2,5,null,1,3,4,null,null,8,3,6,9,null,1,null,null,null,null,9,7,5,2,null,5,null,6,4,5,null,1,2,0,6,null,1,6,null,null,5,null,7,8,4,7,8,6,4,null,5,6,7,9,1,0,4,null,null,null,6,4,8,4,5,null,0,4,4,0,1,7,1,null,1,null,3,6,null,null,null,null,8,null,5,0,7,5,null,null,5,8,null,null,3,null,null,8,null,2,4,null,null,null,null,null,null,null,9,null,9,null,9,null,null,null,null,7,1,null,null,2,null,null,5,5,5,5,6,4,null,null,1,6,4,0,null,0,6,3,0,null,5,5,null,null,null,null,2,null,3,6,null,3,0,5,0,1,0,3,4,9,9,2,7,3,8,6,9,null,5,8,null,null,null,null,9,8,0,7,null,null,8,8,6,6,0,2,7,4,2,3,8,6,4,null,8,null,null,null,2,0,null,1,3,5,4,2,2,5,8,8,null,3,0,null,1,6,0,null,null,9,null,2,null,6,8,2,null,null,5,null,null,null,9,6,6,4,2,0,null,null,1,null,0,null,null,null,6,6,null,null,null,4,7,9,null,0,1,null,null,9,null,null,null,4,null,8,null,null,null,null,null,null,4,null,6,null,3,null,null,5,1,2,5,null,0,7,8,null,7,null,null,4,null,4,4,null,2,null,6,null,null,null,7,null,null,null,null,6,4,null,6,null,6,9,null,null,null,9,6,null,9,null,3,null,2,null,7,7,null,null,0,null,6,3,null,null,null,null,null,null,1,null,null,null,6,9,7,null,7,null,9,3,3,null,null,null,null,4,null,null,3,null,null,null,3,9,null,0,3,1,9,6,7,9,4,8,null,null,6,null,1,3,7,null,null,null,3,null,2,null,8,1,1,null,null,6,null,7,3,5,null,6,3,4,null,null,5,7,1,null,null,6,4,6,null,null,null,null,5,7,0,7,0,null,5,8,5,5,4,5,null,null,null,null,null,null,1,7,null,null,7,null,9,9,6,4,null,null,3,2,1,null,0,null,0,6,null,null,null,1,5,null,null,null,8,null,null,null,null,3,4,8,null,null,9,6,4,null,null,null,null,8,9,null,1,null,null,null,7,null,null,null,null,null,9,null,null,null,4,1,6,7,0,null,null,null,7,null,null,8,null,null,null,null,null,null,null,4,null,9,null,null,null,null,3,0,6,null,5,null,9,9,null,null,4,3,4,null,null,null,null,8,null,5,null,null,null,null,5,2,null,null,null,null,null,null,null,2,null,null,2,1,8,5,null,0,null,0,3,2,4,5,null,null,null,null,null,7,null,null,0,null,0,null,null,null,0,3,9,null,null,null,null,5,null,null,0,5,0,0,null,9,null,null,null,null,null,null,null,null,8,null,9,3,5,9,0,5,9,null,null,9,4,null,0,2,0,null,null,7,null,7,null,5,7,8,7,null,null,null,3,0,3,null,null,null,null,null,4,5,null,null,2,3,null,2,null,null,7,null,null,9,null,null,9,7,1,null,null,1,6,1,8,null,null,5,null,null,3,7,9,6,null,null,null,null,1,null,null,null,3,7,3,2,3,3,null,1,null,null,null,1,null,null,4,3,4,8,7,null,0,3,0,null,1,1,null,null,null,null,null,5,null,6,0,null,3,1,null,6,null,null,4,0,1,null,6,1,null,null,9,6,4,9,0,8,9,3,3,6,null,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,8,5,8,3,5,4,null,6,null,0,null,null,6,null,4,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,7,3,null,null,1,null,2,4,null,null,null,6,null,null,null,6,null,5,null,null,null,null,1,null,null,3,null,1,null,7,1,null,null,7,1,3,4,8,null,null,null,null,null,4,null,null,4,null,null,null,7,null,6,null,null,1,null,null,null,7,3,3,null,null,null,null,3,0,null,null,4,null,null,null,null,null,null,null,null,null,null,8,null,null,9,null,null,6,6,5,2,null,8,3,8,null,null,null,null,6,7,0,null,null,null,null,1,1,5,null,0,5,null,5,null,null,null,1,2,null,2,9,1,null,2,4,1,null,null,null,1,8,4,4,5,2,null,null,6,4,7,5,2,9,null,4,null,null,null,null,null,3,null,null,5,9,null,null,null,null,9,null,9,null,null,null,2,null,1,9,null,null,null,null,null,1,9,3,null,null,1,9,null,5,2,1,0,null,null,1,9,8,4,7,null,null,5,7,null,null,null,null,1,2,8,null,6,0,null,null,null,null,0,null,null,null,6,null,2,3,0,9,null,null,1,4,6,null,8,null,null,5,null,3,0,null,6,null,null,null,null,null,2,null,null,null,null,null,null,2,5,8,6,9,null,null,null,8,null,null,9,6,null,null,null,null,3,null,null,null,null,9,null,null,2,null,null,null,null,null,null,8,8,null,null,null,null,null,9,null,6,null,2,5,null,null,1,2,null,4,null,null,4,null,null,3,5,null,3,3,null,null,1,null,null,null,null,4,null,2,3,null,4,5,3,null,7,null,null,null,7,6,null,null,1,3,null,4,9,8,null,null,0,null,3,4,null,8,null,1,null,null,2,2,null,null,4,null,null,null,3,null,null,2,null,null,null,4,null,5,null,null,null,null,2,null,5,null,null,null,null,null,null,2,7,5,null,6,null,null,null,null,2,null,0,null,3,null,1,null,9,4,null,3,null,null,null,null,null,null,null,5,5,7,null,null,1,null,4,6,null,null,null,2,null,5,9,0,6,2,null,null,null,null,null,null,null,null,null,null,null,null,5,null,7,null,2,9,null,null,1,null,null,null,1,6,null,6,null,null,0,8,null,4,null,null,null,null,4,null,null,0,null,6,0,null,null,null,4,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,0,5,4,2,6,4,5,3,4,null,null,5,null,null,null,null,4,null,null,3,6,2,0,null,6,6,null,null,null,null,0,6,null,null,null,3,9,4,null,null,null,null,null,0,null,null,6,7,0,null,9,2,null,3,3,null,null,8,null,3,null,null,null,8,5,3,null,2,4,null,9,6,9,null,null,null,null,6,null,6,null,5,3,null,null,null,null,4,null,null,null,9,0,9,7,1,1,null,1,null,1,6,null,5,null,6,null,null,1,null,null,null,null,null,null,5,null,null,null,null,null,3,null,6,1,null,0,2,null,null,0,null,null,0,null,null,null,null,null,3,null,null,8,null,null,5,3,3,null,null,null,null,null,null,null,3,null,null,0,8,7,null,null,8,1,null,null,null,null,null,null,7,null,null,null,null,null,null,null,null,null,null,null,5,2,null,2,6,null,null,null,null,null,null,null,1,5,0,null,null,2,null,7,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,8,null,null,null,null,3,null,null,4,null,null,2,null,null,null,null,0,3,null,null,null,null,null,7,null,8,null,null,null,null,8,5,null,3,4,null,null,null,8,null,null,null,null,null,null,null,null,null,3,7,null,null,null,4,0,3,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,8,null,null,null,null,null,2,null,null,null,null,null,null,null,null,null,0,null,null,null,2,null,null,null,8,2,null,null,null,null,null,null,null,8,null,null,null,null,null,null,null,null,null,null,2,null,null,null,2,5,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,8,null,null,null,null,null,null,null,null,null,null,0,5])) # 2
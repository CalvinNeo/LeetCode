# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = None
        def index(cur):
            cntl = 0
            cntr = 0
            if cur.left:
                cntl = index(cur.left)
            if cur.right:
                cntr = index(cur.right)
            return cntl + 1 + cntr

        def dfs(cur, kk):
            # print "find {}-th at {}".format(kk, cur.val)
            cntl = 0
            if cur.left:
                cntl = index(cur.left)
                if kk <= cntl:
                    return dfs(cur.left, kk)
            if kk == cntl + 1:
                return cur.val
            return dfs(cur.right, kk - cntl - 1)

        return dfs(root, k)

sln = Solution()
print sln.kthSmallest(make_tree([1, null, 2]), 2)
print sln.kthSmallest(make_tree([2,1]), 1)
print sln.kthSmallest(make_tree([3,1,4,null,2]), 4)
print sln.kthSmallest(make_tree([3,1,4,null,2]), 2)
print sln.kthSmallest(make_tree([3,1,4,null,2]), 3)
print sln.kthSmallest(make_tree([3,1,4,null,2]), 1)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def isb(cur, deep):
            lh, rh = deep, deep
            if not cur.left and not cur.right:
                return True, deep
            f = True
            if cur.left:
                f, lh = isb(cur.left, deep + 1)
            if not f:
                return False, 0
            if cur.right:
                f, rh = isb(cur.right, deep + 1)
            if not f:
                return False, 0
            if abs(lh - rh) > 1:
                # print "fail at", cur.val, "where lh = {}, rh = {}".format(lh, rh)
                return False, 0
            return True, max(lh, rh)
        return isb(root, 0)[0]

sln = Solution()
N = [3,9,20,None,None,15,7]
N1 = TreeNode(0)
build_tree(N, N1, 0)
print sln.isBalanced(N1)
N = [1,2,2,3,3,null,null,4,4]
N1 = TreeNode(0)
build_tree(N, N1, 0)
print sln.isBalanced(N1)
N = [1,2,3,4,5,null,6,7]
N1 = TreeNode(0)
build_tree(N, N1, 0)
print sln.isBalanced(N1)

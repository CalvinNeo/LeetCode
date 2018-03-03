#coding: utf8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys

        if root == None:
            return True

        def validate(cur, lb, rb):
            flag = True
            if cur.left:
                # 最大值有限制
                if lb < cur.left.val < cur.val:
                    flag = flag and validate(cur.left, lb, cur.val)
                else:
                    return False

            if not flag:
                return flag

            if cur.right:
                # 最小值有限制
                if cur.val < cur.right.val < rb: # 注意这里的cur.val
                    flag = flag and validate(cur.right, cur.val, rb)
                else:
                    return False

            return flag

        return validate(root, -sys.maxint, sys.maxint)

# sln = Solution()

# N = [10,5,15]
# N = [10,5,15,None,None,6,20]
# N = [3,1,None,None,2,4,6]
# N = [1,1]
# T = TreeNode(0)
# build_tree(N, T, 0)

# print sln.isValidBST(T)
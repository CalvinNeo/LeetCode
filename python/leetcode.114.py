#coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        def dfs(nd):
            prev_right = nd.right
            prev_left = nd.left
            # 先把左子树嫁接过去
            nd.right = nd.left
            # print "at {} move {} to right".format(nd.val, None if prev_left is None else prev_left.val, None if prev_right is None else prev_right.val)
            # 一律清空左儿子
            nd.left = None
            last = nd
            # 如果有左子树，就把左子树的last算出来，如果没有左子树，那么右子树直接连接到nd上
            if not prev_left is None:
                last = dfs(prev_left)
            # print "nd {} last {}".format(nd.val, last.val)
            if prev_right is None:
                # 如果没有右子树，则返回自己？
                # 不，返回左子树的last，在这里WA了一次
                return last
            else:
                last.right = prev_right
                # 否则递归返回右子树的last
                return dfs(prev_right)

        dfs(root)
        return root

sln = Solution()
# t = make_tree([1,2,null,3,4,5])
# t = make_tree([1,2,5,3,4,null,6])
t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.left.left.left = TreeNode(5)
print_tree(t)
print "====================="
print_tree(sln.flatten(t))
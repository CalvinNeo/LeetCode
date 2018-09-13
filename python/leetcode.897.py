# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nt = TreeNode(None)
        self.ntc = self.nt

        def inorder(cur):
            if cur.left:
                inorder(cur.left)
            self.ntc.right = TreeNode(cur.val)
            self.ntc = self.ntc.right
            if cur.right:
                inorder(cur.right)

        inorder(root)
        return self.nt.right


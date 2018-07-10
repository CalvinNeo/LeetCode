# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(postorder)
        if n == 1:
            return TreeNode(postorder[0])
        elif n == 0:
            return None

        root = postorder[-1]
        index_root_inorder = inorder.index(root)
        left_inorder = inorder[0:index_root_inorder]
        right_inorder = inorder[index_root_inorder+1:]
        j = n - 2
        while j >= 0:
            if postorder[j] in left_inorder:
                break
            j -= 1
        left_postorder = postorder[0:j+1]
        right_postorder = postorder[j+1:n-1]
        # print left_inorder, left_postorder, right_inorder, right_postorder
        left_node = self.buildTree(left_inorder, left_postorder)
        right_node = self.buildTree(right_inorder, right_postorder)
        root_node = TreeNode(postorder[-1])
        root_node.left = left_node
        root_node.right = right_node
        return root_node

sln = Solution()
# print_tree(sln.buildTree([9,3,15,20,7], [9,15,7,20,3]), 0)
print_tree(sln.buildTree([2,1], [2,1]), 0)
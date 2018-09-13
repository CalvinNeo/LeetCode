# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        mx = max(nums)
        index = nums.index(mx)
        root = TreeNode(mx)
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:n])

        return root

# sln = Solution()
# print_tree( sln.constructMaximumBinaryTree([3,2,1,6,0,5]), 0 )
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(nd):
            if nd == None:
                return
            if nd.left == None and nd.right == None:
                return
            if nd.left == None:
                dfs(nd.right)
                if nd.right.val < nd.val:
                    nd.left, nd.right = nd.right, nd.left
            elif nd.right == None:
                dfs(nd.left)
                if nd.left.val > nd.val:
                    nd.left, nd.right = nd.right, nd.left
            else:
                dfs(nd.left)
                dfs(nd.right)
                if nd.left.val > nd.right.val:
                    nd.left, nd.right = nd.right, nd.left

        dfs(root)

sln = Solution()
root = TreeNode(0)
x1 = TreeNode(1)
root.left = x1
sln.recoverTree(root)
print root.val,  root.right.val
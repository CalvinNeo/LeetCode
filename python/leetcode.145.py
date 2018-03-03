# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ans = []
        def tr(cur):
            if cur.left:
                tr(cur.left)
            if cur.right:
                tr(cur.right)
            ans.append(cur.val)
        tr(root)
        return ans
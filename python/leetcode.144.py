# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def recur(root, ans):
            if root:
                ans.append(root.val)
                recur(root.left, ans)
                recur(root.right, ans)
        recur(root, ans)
        return ans

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stk = []
        if root != None:
            stk.append(root)
        while len(stk) > 0:
            cur = stk[-1]
            stk.pop()
            print "cur.val", cur.val
            ans.append(cur.val)
            if cur.right:
                stk.append(cur.right)
            if cur.left:
                stk.append(cur.left)
        return ans


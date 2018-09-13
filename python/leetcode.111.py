# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import Queue
        q = Queue.Queue()
        if not root:
            return 0
        q.put((root, 1))
        while not q.empty():
            x, d = q.get()
            if not x.left and not x.right:
                return d
            if x.left:
                q.put((x.left, d+1))
            if x.right:
                q.put((x.right, d+1))
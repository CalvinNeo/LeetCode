# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = Queue.Queue()

        q.put((root, 1))

        ans = []
        prevd = 0
        while not q.empty():
            nd, d = q.get()
            if d != prevd:
                ans.append(nd.val)
                prevd = d
            else:
                ans[-1] = nd.val
            if nd.left:
                q.put((nd.left, d + 1))
            if nd.right:
                q.put((nd.right, d + 1))
        return ans

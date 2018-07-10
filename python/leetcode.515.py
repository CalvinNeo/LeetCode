# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = Queue.Queue()
        if not root:
            return []
        inf = 5555555555
        ans = []
        prevd = 0
        q.put((root, 1))
        while q.qsize() > 0:
            nd, d = q.get()
            if d != prevd:
                prevd = d
                ans.append(nd.val)
            else:
                ans[-1] = max(ans[-1], nd.val)

            if nd.left:
                q.put((nd.left, d + 1))
            if nd.right:
                q.put((nd.right, d + 1))
        return ans
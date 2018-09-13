# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import Queue
        q = Queue.Queue()

        if not root:
            return 0

        q.put((root, 0, 1))

        prev = -1
        mi = -1
        ans = 0
        mx = -1
        while not q.empty():
            nd, d, index = q.get()
            if prev != d:
                # print "mx {} mi {} d {}".format(mx, mi, d)
                ans = max(ans, mx - mi + 1)
                prev = d
                mi = index

            mx = index
            if nd.left:
                q.put((nd.left, d + 1, index * 2))
            if nd.right:
                q.put((nd.right, d + 1, index * 2 + 1))

        # print "mx {} mi {}".format(mx, mi)
        if mx != mi:
            ans = max(ans, mx - mi + 1)
        return ans

# sln = Solution()
# print sln.widthOfBinaryTree(make_tree([1,3,2,5,3,null,9]))
# print sln.widthOfBinaryTree(make_tree([1,3,null,5,3]))
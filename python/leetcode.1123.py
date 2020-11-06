# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import Queue
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = Queue.Queue()
        if root == None:
            return root
        dm = {}
        dmmax = 0
        lookup = {}
        q.put((root, 1, None))
        while not q.empty():
            nd, d, fa = q.get()
            lookup[nd.val] = fa
            if not d in dm:
                dm[d] = [nd, None]
            else:
                dm[d][1] = nd
            dmmax = d
            if nd.left:
                q.put((nd.left, d + 1, nd))
            if nd.right:
                q.put((nd.right, d + 1, nd))

        def get_lst(st):
            ans = []
            while st != None:
                ans.append(st)
                st = lookup[st.val]
            return reversed(ans)

        if dm[dmmax][1] == None:
            return dm[dmmax][0]
        else:
            l0 = get_lst(dm[dmmax][0])
            l1 = get_lst(dm[dmmax][1])
            z = zip(l0, l1)
            l = len(z)
            for i in xrange(l - 1, -1, -1):
                if z[i][0].val == z[i][1].val:
                    return z[i][0]

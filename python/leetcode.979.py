# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(nd):
            nd.node_count = 1
            nd.coin_count = nd.val
            if nd.left:
                ln, lc = dfs(nd.left)
                nd.node_count += ln
                nd.coin_count += lc
            if nd.right:
                rn, rc = dfs(nd.right)
                nd.node_count += rn
                nd.coin_count += rc
            return nd.node_count, nd.coin_count

        if not root:
            return 0

        dfs(root)

        def dfs2(nd):
            gap = 0
            if nd.left:
                x = abs(nd.left.node_count - nd.left.coin_count)
                # print "L", nd.val, x
                gap += x
                gap += dfs2(nd.left)
            if nd.right:
                x = abs(nd.right.node_count - nd.right.coin_count)
                # print "R", nd.val, x
                gap += x
                gap += dfs2(nd.right)
            return gap

        return dfs2(root)

from utils import *
sln = Solution()
# print sln.distributeCoins(make_tree([3,0,0])) # 2
# print sln.distributeCoins(make_tree([0,3,0])) # 3
print sln.distributeCoins(make_tree([1,0,0,null,3])) # 4

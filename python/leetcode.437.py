# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def make_sum_tree(tree, cur_sum):
            if tree:
                sum_tree = TreeNode(cur_sum + tree.val)

                if tree.left:
                    sum_tree.left = make_sum_tree(tree.left, cur_sum + tree.val)

                if tree.right:
                    sum_tree.right = make_sum_tree(tree.right, cur_sum + tree.val)

                return sum_tree
            return None

        st = make_sum_tree(root, 0)

        self.ans = 0
        d = {0:1}
        def dfs(cur):
            if not cur:
                return

            need = cur.val - sum
            # Important ` d[need] > 0`
            if need in d and d[need] > 0:
                # print "ans ++ at cur.val = {}, need {}".format(cur.val, cur.val - sum)
                # Important ` += d[need]` not `+=1`
                self.ans += d[need]

            if not cur.val in d:
                d[cur.val] = 0
            d[cur.val] += 1

            dfs(cur.left)
            dfs(cur.right)

            d[cur.val] -= 1
        dfs(st)

        return self.ans

# sln = Solution()
# print sln.pathSum(make_tree([10,5,-3,3,2,null,11,3,-2,null,1]), 8) # 3
# print sln.pathSum(make_tree([1]), 0) # 0
# print sln.pathSum(make_tree([1,-2,-3]), -1) # 1
# print sln.pathSum(make_tree([0,1,1]), 1) # 4

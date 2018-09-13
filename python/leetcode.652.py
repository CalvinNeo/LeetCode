# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.s = set()
        self.s2 = set()
        self.t = []

        if not root:
            return []

        def dfs1(cur):
            l = ""
            if cur.left:
                l = dfs1(cur.left)
            r = ""
            if cur.right:
                r = dfs1(cur.right)

            me = "({}#{}#{})".format(l, cur.val, r)
            

            if me in self.s and me not in self.s2:
                print me
                self.t.append(cur)
                self.s2 |= set([me])
            self.s |= set([me])
            return me

        dfs1(root)

        # print self.s
        return self.t

# sln = Solution()
# T = make_tree([1,2,3,4,null,2,4,null,null,null,null,4])
# print_tree(T, 0)
# print sln.findDuplicateSubtrees(make_tree([0,0,0,0,null,null,0,null,null,null,0]))
# print sln.findDuplicateSubtrees(make_tree([1,2,3,4,null,2,4,null,null,null,null,4]))
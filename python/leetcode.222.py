# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *
class Solution(object):
    # def countNodesImpl(self, root):
    #     ans = 0
    #     isfulll = 0
    #     isfullr = 0
    #     if root.left:
    #         cl, isfulll = self.countNodesImpl(root.left)
    #         ans += cl
    #     if root.right:
    #         cr, isfullr = self.countNodesImpl(root.right)
    #         ans += cr
    #     isfull = 0
    #     if isfulll and isfullr:
    #         isfull = 1
    #     elif not root.left and not root.right:
    #         isfull = 1
    #     if isfull:
    #         ans += 1
    #     print "Node {}".format(root.val), ans, isfull
    #     return ans, isfull

    def countNodesWA(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.ans = 0
        def dfs(cur):
            # print "cur", cur.val
            if cur.right:
                nxt = dfs(cur.right)
                if nxt:
                    dfs(cur.left)
            else:
                if cur.left:
                    dfs(cur.left)
                    return 1
                else:
                    # A possible answer
                    self.ans = max(self.ans, cur.val)
                    return 1

        dfs(root)
        return self.ans


    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(cur):
            if not cur:
                return 0

            hl = 0
            t = cur
            while t:
                hl += 1
                t = t.left

            t = cur
            hr = 0
            while t:
                hr += 1
                t = t.right
            
            if hl == hr:
                return 2 ** hl - 1
            else:
                return dfs(cur.left) + dfs(cur.right) + 1

        return dfs(root)

# sln = Solution()
# print sln.countNodes(None) # 0
# print sln.countNodes(make_tree([1,2,3,4,5,6])) # 6
# print sln.countNodes(make_tree([1,2,3,4])) # 4

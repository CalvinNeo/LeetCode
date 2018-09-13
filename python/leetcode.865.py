# 866 c92.2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils import *

import Queue
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.max_deep = 0
        def find_deep(cur, deep):
            self.max_deep = max(deep, self.max_deep)
            if cur.left:
                find_deep(cur.left, deep + 1)
            if cur.right:
                find_deep(cur.right, deep + 1)

        lst = []
        lnk = []
        def dfs(cur, deep):
            lnk.append(cur)
            if deep == self.max_deep:
                lst.append(list(lnk))
            if cur.left:
                dfs(cur.left, deep + 1)
            if cur.right:
                dfs(cur.right, deep + 1)
            lnk.pop()

        def make_ans():
            l = 0
            while 1:
                finish = 0
                cm = None
                for i, lk in enumerate(lst):
                    if not (l < len(lk)):
                        finish = 1
                        break
                    if i == 0:
                        cm = lk[l]
                    else:
                        if cm.val != lk[l].val:
                            finish = 1
                            break
                if finish:
                    break
                else:
                    l += 1
            l -= 1
            return lst[0][l]

        if not root:
            return None
        find_deep(root, 0)
        dfs(root, 0)
        # print lst
        return make_ans()

sln = Solution()
print_tree(sln.subtreeWithAllDeepest(make_tree([3,5,1,6,2,0,8,null,null,7,4])))
print_tree(sln.subtreeWithAllDeepest(make_tree([1])))
print sln.subtreeWithAllDeepest(None)
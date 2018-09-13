
from utils import *

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def pr(cur):
            if not cur.left and not cur.right:
                return cur.val == 1

            has_1 = 0
            if cur.left:
                l = pr(cur.left)
                has_1 = has_1 or l
                if not l:
                    cur.left = None

            if cur.right:
                l = pr(cur.right)
                has_1 = has_1 or l
                if not l:
                    cur.right = None

            if not (has_1 or cur.val == 1):
                return 0
            else:
                return 1

        if not pr(root):
            root = None
        return root

sln = Solution()
# print_tree(make_tree([1,0,0,null,null,0,1]), 0)
print_tree( sln.pruneTree(make_tree([1,0,0,null,null,0,1])), 0 )
print_tree( sln.pruneTree(make_tree([1,1,0,1,1,0,1,0])), 0 )
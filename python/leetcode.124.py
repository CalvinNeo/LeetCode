# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def print_tree(root, dep):
    print "{}{}".format("\t"*dep, root.val)
    if root.left != None:
        print_tree(root.left, dep+1)
    if root.right != None:
        print_tree(root.right, dep+1)

def build_tree(n, root, p):
    # change root in-place
    root.val = n[p]
    lson = 2 * p + 1
    rson = 2 * p + 2
    if lson < len(n) and n[lson] != None:
        root.left = TreeNode(0)
        build_tree(n, root.left, lson)
    if rson < len(n) and n[rson] != None:
        root.right = TreeNode(0)
        build_tree(n, root.right, rson)

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs1(t, tdebug):
            left = 0
            right = 0
            if t.left != None:
                tdebug.left = TreeNode(0)
                left = dfs1(t.left, tdebug.left)

            if t.right != None:
                tdebug.right = TreeNode(0)
                right = dfs1(t.right, tdebug.right)

            tdebug.val = max([t.val, left + t.val, right + t.val]) 
            return tdebug.val

        def dfs2(t, tdebug, choices):
            # left = 0
            # if t.left != None:
            #     left = dfs2(t.left, tdebug.left)
            # right = 0
            # if t.right != None:
            #     right = dfs2(t.right, tdebug.right)
            # print t.val, "++", [res, left, right, left + t.val + right]
            if t.left != None:
                dfs2(t.left, tdebug.left, choices)
            if t.right != None:
                dfs2(t.right, tdebug.right, choices)

            choices.append(t.val)

            if tdebug.left != None and tdebug.right != None:
                choices.append(tdebug.right.val + t.val + tdebug.left.val)
            if tdebug.left != None:
                choices.append(tdebug.left.val + t.val)
            if tdebug.right != None:
                choices.append(tdebug.right.val + t.val)

        rootdebug = TreeNode(0)
        dfs1(root, rootdebug)
        import sys
        # print_tree(rootdebug, 0)
        # print "================================="
        choices = [-sys.maxint]
        dfs2(root, rootdebug, choices)
        # print choices
        # print choices
        res = max(choices)
        return res

N1 = TreeNode(1)
N2 = TreeNode(2)
N3 = TreeNode(3)
N1.left = N2
N1.right = N3

N1 = TreeNode(2)
N2 = TreeNode(-1)
N1.left = N2

N1 = TreeNode(-1)
N2 = TreeNode(2)
N3 = TreeNode(3)
N4 = TreeNode(4)
N1.left = N2
N2.left = N3
N2.right = N4

N1 = TreeNode(-2)
N2 = TreeNode(-1)
N1.left = N2

N = [1,-2,-3,1,3,-2,None,-1]
N1 = TreeNode(0)
build_tree(N, N1, 0)

N = [1, -2, 3]
N1 = TreeNode(0)
build_tree(N, N1, 0)

sln = Solution()
print sln.maxPathSum(N1)
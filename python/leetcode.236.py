# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    fa = dict()

    def find(v):
        if not v in fa:
            fa[v] = v
        if fa[v] == v:
            return v
        else:
            return find(fa[v])

    def merge(a, b):
        aa = find(a)
        bb = find(b)
        if aa != bb:
            fa[aa] = bb

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
N = [1,2,3,4,5]
N = [1,2,None,3]
N1 = TreeNode(0)
build_tree(N, N1, 0)

sln = Solution()

print sln.lowestCommonAncestor(N1, N1.left.left, N1).val
print sln.lowestCommonAncestor(N1, N1.left.left, N1.right).val
print sln.lowestCommonAncestor(N1, N1.left.right, N1.right).val

# N = [-1,0,3,-2,4,None,None,8]
# N1 = TreeNode(0)
# build_tree(N, N1, 0)
# print sln.lowestCommonAncestor(N1, N1.left, N1.left.left.left).val # 0

# N = [3,5,1,6,2,0,8,None,None,7,4]
# N1 = TreeNode(0)
# build_tree(N, N1, 0)
# print sln.lowestCommonAncestor(N1, N1.left, N1.left.right.right).val # 5

# N = [3,5,1,6,2,0,8,None,None,7,4]
# N1 = TreeNode(0)
# build_tree(N, N1, 0)
# print sln.lowestCommonAncestor(N1, N1.left, N1.right).val # 3

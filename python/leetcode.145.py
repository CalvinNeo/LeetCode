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
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ans = []
        def tr(cur):
            if cur.left:
                tr(cur.left)
            if cur.right:
                tr(cur.right)
            ans.append(cur.val)
        tr(root)
        return ans

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stk = []

        if root == None:
            return []

        cur = root
        def copy(t):
            r = TreeNode(t.val)
            r.left = t.left
            r.right = t.right
            return r

        while True:
            while cur != None:
                stk.append(cur)
                if cur.left:
                    cur = cur.left
                else:
                    break

            while len(stk) > 0:
                cur = stk[-1]
                stk.pop()
                if cur.right:
                    # choose the right node
                    oldcur = copy(cur)
                    # reuse stk, must reset right to None to avoid repeated selection
                    cur.right = None
                    # for cur itself
                    stk.append(cur)
                    cur = oldcur.right
                    break
                else:
                    # no left and no right
                    ans.append(cur.val)
                    cur = None

            if len(stk) == 0 and cur == None:
                break

        return ans

sln = Solution()
N = [1, None, 2, None, None, 3, None]
N = [2, 3, None, 1]
N1 = TreeNode(0)
build_tree(N, N1, 0)
print sln.postorderTraversal(N1)
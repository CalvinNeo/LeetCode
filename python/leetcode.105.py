# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        n = len(preorder)
        root = preorder[0]
        root_node = TreeNode(root)

        if n > 1:
            mid_index = inorder.index(root)
            left_inorder = inorder[:mid_index]
            right_inorder = inorder[mid_index+1:]

            rs = set(right_inorder)

            split = 0
            for i in xrange(1, n):
                if preorder[i] in rs:
                    split = i
                    break

            if not preorder[n - 1] in rs:
                split = n

            left_preorder = preorder[1:split]
            right_preorder = preorder[split:]

            # print "Handle root {} left_inorder {} right_inorder {} left_preorder {} right_preorder {} split {}".format(root, left_inorder, right_inorder, left_preorder, right_preorder, split)

            left_nd = self.buildTree(left_preorder, left_inorder)
            right_nd = self.buildTree(right_preorder, right_inorder)
            root_node.left = left_nd
            root_node.right = right_nd

        return root_node

sln = Solution()
# print sln.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print sln.buildTree(preorder = [1,2], inorder = [2,1])
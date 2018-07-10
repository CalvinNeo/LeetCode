# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import Queue
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = Queue.Queue()
        cur_deep = 1
        cur_ans = root.val
        q.put((root, 1))
        while q.qsize() > 0:
            nd, deep = q.get()
            if deep != cur_deep:
                cur_deep = deep
                cur_ans = nd.val
            if nd.left:
                q.put((nd.left, deep + 1))
            if nd.right:
                q.put((nd.right, deep + 1))
        return cur_ans

# sln = Solution()
# print sln.findBottomLeftValue(make_tree([1])) # 1
# print sln.findBottomLeftValue(make_tree([2,1,3])) # 1
# print sln.findBottomLeftValue(make_tree([1,2,3,4,null,5,6,null,null,null,null,7])) # 7
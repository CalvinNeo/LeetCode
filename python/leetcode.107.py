# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import Queue
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        q = Queue.Queue()
        q.put( (root, 0) )
        ans = []
        prevd = None
        while not q.empty():
            (cur, d) = q.get()
            if prevd == None or d == prevd:
                if ans == []:
                    ans.append([cur.val])
                else:
                    ans[-1].append(cur.val)
            else:
                ans.append([cur.val])
            prevd = d
            if cur.left:
                q.put((cur.left, d + 1))
            if cur.right:
                q.put((cur.right, d + 1))

        return list(reversed(ans))

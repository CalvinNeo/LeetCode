# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

import Queue
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        q = Queue.Queue()
        if not root:
            return
        q.put((root, 0))

        prev = None
        curd = -1
        while not q.empty():
            nd, d = q.get()
            if d != curd:
                # new line
                curd = d
            else:
                if prev:
                    prev.next = nd
            if nd.left:
                q.put((nd.left, d + 1))
            if nd.right:
                q.put((nd.right, d + 1))
            prev = nd
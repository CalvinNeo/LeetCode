# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            if node.next is not None:
                node.val = node.next.val
                if node.next.next is None:
                    node.next = None
                    return
                else:
                    node = node.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import *

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur:
            i = cur.next
            if i and i.val == cur.val:
                while i and i.val == cur.val:
                    i = i.next
                if prev == None:
                    head = i
                else:
                    prev.next = i
                cur = i
            else:
                prev = cur
                cur = cur.next
        return head

# sln = Solution()
# print_linked(sln.deleteDuplicates(make_linked([])))
# print_linked(sln.deleteDuplicates(make_linked([1])))
# print_linked(sln.deleteDuplicates(make_linked([1,2,3,3,4,4,5])))
# print_linked(sln.deleteDuplicates(make_linked([1,1,1,2,3])))
# print_linked(sln.deleteDuplicates(make_linked([1,1,1])))
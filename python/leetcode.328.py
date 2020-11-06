# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import *

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def solve(odd, even):
            nxt_odd = None
            if even:
                nxt_odd = even.next
            nxt_even = None
            if nxt_odd:
                nxt_even = nxt_odd.next
            if odd:
                odd.next = nxt_odd
            if even:
                even.next = nxt_even
            return nxt_odd, nxt_even

        if not head:
            return None
        ho, he = head, head.next
        o, e = ho, he
        to, te = ho, he
        while o or e:
            o, e = solve(o, e)
            if o:
                to = o
            if e:
                te = e
        to.next = he
        if te:
            te.next = None
        return ho

# sln = Solution()
# print_linked(sln.oddEvenList(make_linked([1,2,3,4,5])))
# print_linked(sln.oddEvenList(make_linked([1])))
# print_linked(sln.oddEvenList(make_linked([1,2])))
# print_linked(sln.oddEvenList(make_linked([2,1,3,5,6,4,7])))
# print_linked(sln.oddEvenList(None))
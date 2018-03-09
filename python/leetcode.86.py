# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # important, don't set to None, it will result in pass-by-value
        lesser = ListNode(None)
        greater = ListNode(None)
        equal = ListNode(None)
        ll = lesser
        gg = greater
        ee = equal
        cur = head
        def set_to(l, x):
            if l:
                l.next = x
            else:
                l = x
            return x

        while cur:
            if cur.val < x:
                ll.next = cur
                ll = ll.next
            # elif cur.val == x:
            #     ee.next = cur
            #     ee = ee.next
            else:
                gg.next = cur
                gg = gg.next
            cur = cur.next

        ans = ListNode(0)
        tail = ans
        # print_linked(lesser)
        if lesser.next:
            tail.next = lesser.next
            tail = ll
            # important
            tail.next = None
        # if equal.next:
        #     tail.next = equal.next
        #     tail = ee
        #     tail.next = None
        if greater.next:
            tail.next = greater.next
            tail = gg
            tail.next = None
        return ans.next

def print_linked(x):
    while x:
        print x.val, " ", 
        x = x.next


sln = Solution()
l = [ListNode(2), ListNode(1), ListNode(1), ListNode(1), ListNode(5)]
l[0].next = l[1]
l[2].next = l[3]
print_linked(sln.partition(l[0], 1))
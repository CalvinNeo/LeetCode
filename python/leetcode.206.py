# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Iterative
        cur = head
        prev = None
        while True:
            if cur == None:
                return prev
            if prev == None:
                next = cur.next
                cur.next = None
                prev = cur
                cur = next
                continue

            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursive
        if head == None:
            return None
        def rev(h):
            next = h.next
            if next == None:
                return h, h
            myprev, newhead = rev(next)
            myprev.next = h
            return h, newhead
        _, newhead = rev(head)
        head.next = None
        return newhead


def print_linked(head):
    while head != None:
        print head.val, " ",
        head = head.next

sln = Solution()
l = [ListNode(0), ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)]
l[0].next = l[1]
l[1].next = l[2]
l[2].next = l[3]

head = sln.reverseList(l[0])
print_linked(head)
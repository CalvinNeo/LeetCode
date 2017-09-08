# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 1
        ii = head
        if ii == None:
            return None
        while ii.next != None:
            ii = ii.next
            length += 1
        if length == 1:
            return head
        k = (length - k % length) % length
        if k == 0 :
            return head
        newhead = head
        for i in xrange(k):
            newhead = newhead.next
        oldtail = head
        while oldtail.next != None:
            oldtail = oldtail.next
        oldtail.next = head
        newtail = head
        # print newhead.val, oldtail.val, newtail.val
        while newtail.next != newhead:
            newtail = newtail.next
        newtail.next = None
        return newhead

def print_nodes(x):
    while x != None:
        print x.val
        x = x.next

sln = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
print_nodes( sln.rotateRight(n1, 0) )
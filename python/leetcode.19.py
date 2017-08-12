# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        before = ListNode(None)
        to_remove = head
        before.next = to_remove
        end = head
        for x in xrange(n - 1):
            end = end.next
        while end.next != None:
            before = before.next
            to_remove = to_remove.next
            end = end.next
        if before.val == None:
            # head
            return head.next
        else:
            before.next = to_remove.next
            return head
    
sln = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
ans = sln.removeNthFromEnd(n1, 2)
while ans != None:
    print ans.val
    ans = ans.next
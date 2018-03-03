# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp = head
        sp = head
        while fp != None and sp != None:
            fp = fp.next
            if fp == None:
                return False
            fp = fp.next
            sp = sp.next
            if fp == sp:
                return True
        return False

sln = Solution()
print sln.hasCycle(ListNode(1))
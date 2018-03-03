# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = None
        fp = head
        sp = head
        t = 0
        c = 0
        meet_node = None
        while fp != None and sp != None:
            fp = fp.next
            if fp == None:
                return None
            fp = fp.next
            sp = sp.next

            if meet_node != None:
                c += 1

            if fp == sp:
                if meet_node == None:
                    meet_node = fp
                else:
                    break

        fp = meet_node
        sp = head
        while fp != None and sp != None:
            if fp == sp:
                return fp
            fp = fp.next
            sp = sp.next
        return None

sln = Solution()
l = [ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)]
l[0].next = l[1]
l[1].next = l[2]
l[2].next = l[3]
l[3].next = l[4]
l[4].next = l[2]
print sln.detectCycle(l[0]).val
l[0].next = l[1]
l[1].next = l[0]
print sln.detectCycle(l[0]).val
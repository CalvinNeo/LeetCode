# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        llast = headA
        if headA == None or headB == None:
            return None
            
        while llast.next != None:
            llast = llast.next

        def next(nd):
            if nd == llast:
                return headB
            return nd.next

        def detectCycle(head):
            start = None
            fp = head
            sp = head
            t = 0
            c = 0
            meet_node = None
            while fp != None and sp != None:
                fp = next(fp)
                if fp == None:
                    return None
                fp = next(fp)
                sp = next(sp)

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
                fp = next(fp)
                sp = next(sp)
            return None

        return detectCycle(headA)

sln = Solution()
l = [ListNode(0), ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)]
l[0].next = l[1]
l[1].next = l[2]
l[3].next = l[4]
l[4].next = l[2]
l[2].next = l[5]
l[5].next = l[6]

print sln.getIntersectionNode(l[0], l[3]).val
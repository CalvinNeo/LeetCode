# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = ListNode(None)
        cur = root
        while True:
            nowmin = None
            i = 0
            for nd in lists:
                if nd != None:
                    if nowmin == None:
                        nowmin = i 
                    elif nowmin != None and nd.val < lists[nowmin].val:
                        nowmin = i
                i += 1
            if nowmin == None:
                return root.next
            else:
                cur.next = ListNode(lists[nowmin].val)
                lists[nowmin] = lists[nowmin].next
                cur = cur.next


class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(None)
        cur = root
        while l1 or l2:
            if l1 == None:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val <= l1.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        return root.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        elif len(lists) == 10:
            return lists[0]
        else:
            for i in xrange(0, len(lists) - 1):
                lists[i + 1] = self.mergeTwoLists(lists[i], lists[i + 1])
                lists[i] = None
        return lists[len(lists) - 1]

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(None)
        cur = root
        while l1 or l2:
            if l1 == None:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val <= l1.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        return root.next

    def mergeKListsImpl(self, lists, fr, to):
        if to == fr:
            return lists[fr]
        elif to < fr:
            return None
        else:
            mid = (fr + to) / 2
            ll = self.mergeKListsImpl(lists, fr, mid)
            rr = self.mergeKListsImpl(lists, mid + 1, to)
            return self.mergeTwoLists(ll, rr)

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        return self.mergeKListsImpl(lists, 0, len(lists) - 1)

sln = Solution()
ans =  sln.mergeKLists([ListNode(1), ListNode(3),ListNode(5), ListNode(4)])
while ans != None:
    print ans.val
    ans = ans.next
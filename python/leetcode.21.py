# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
sln = Solution()
#n1 = ListNode(1)
#n2 = ListNode(2)
#n3 = ListNode(3)
#n1.next = n2
#n2.next = n3
n1 = ListNode(1)
ans = sln.mergeTwoLists(ListNode(1), ListNode(2))
while ans != None:
    print ans.val
    ans = ans.next
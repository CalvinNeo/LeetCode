# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        root = ListNode(None)
        root.next = head
        bef = root
        fst = head
        end = head.next
        while fst != None:
            if end == None:
                return root.next
            else:
                bef.next = end
                rear = end.next
                end.next = fst
                fst.next = rear
                bef = fst
                fst = bef.next
                if bef.next == None:
                    end = None
                else:
                    end = bef.next.next
        return root.next

sln = Solution()
nd = [ListNode(1), ListNode(2)]
nd[0].next = nd[1]
ans =  sln.swapPairs(nd[0])
while ans != None:
    print ans.val
    ans = ans.next
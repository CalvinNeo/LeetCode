# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortListTLE(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        tail = head
        while tail.next != None:
            tail = tail.next

        def part(deep, fr, to):
            if fr == None or to == None:
                return
            if fr == to or to.next == fr:
                return
            x = to.val
            i = ListNode(None)
            i.next = fr
            j = fr
            # print "[{}]".format(deep), fr.val, to.val
            while j != to:
                if j.val <= x:
                    i = i.next
                    i.val, j.val = j.val, i.val
                j = j.next

            t = i.next
            t.val, j.val = j.val, t.val

            # print fr.val, i.val, t.next.val, to.val
            part(deep + 1, fr, i)
            part(deep + 1, t.next, to)

        part(0, head, tail)
        return head
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        def part(fr):
            to = fr
            while to.next != None:
                to = to.next

            if fr == None or fr.next == None:
                return fr
            slow = fr
            fast = fr
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            start2 = slow.next
            slow.next = None

            lhead = part(fr)
            rhead = part(start2)

            if not lhead and not rhead:
                return None
            elif not lhead:
                return rhead
            elif not rhead:
                return lhead
            else:
                # merge
                H = ListNode(None)
                C = H
                while lhead and rhead:
                    if lhead.val < rhead.val:
                        C.next = lhead
                        C = C.next
                        lhead = lhead.next
                    else:
                        C.next = rhead
                        C = C.next
                        rhead = rhead.next
                if lhead:
                    C.next = lhead
                elif rhead:
                    C.next = rhead
            return H.next

        return part(head)

def make_list(lst):
    l = None
    h = None
    for x in lst:
        if l:
            l.next = ListNode(x)
            l = l.next
        else:
            l = ListNode(x)
            h = l
    return h

def print_list(lst):
    while lst != None:
        print lst.val, " ", 
        lst = lst.next

sln = Solution()
l1 = make_list([1,3,2,4,6])
l1 = make_list([1,1,2,3,2])
l1 = make_list([1])
l1 = make_list([1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2,1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2])
# l1 = make_list([3,2])
print_list( l1 )
print ""
l2 = sln.sortList(l1)
print_list( l2 )
print ""
print sln.sortList(None)

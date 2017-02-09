import itertools
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
#    def __iter__(self):
#        return self
#    def next(self):
#        if self.next == None:            
#            raise StopIteration()
#        else:
#            return self.next
#    def append(self, ln):
#        self.next = ln
#        return ln

#class Solution(object):
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """
#        r = 0
#        ans = ListNode(0)
#        for x in itertools.izip_longest(l1, l2, fillvalue = 0):
#            inplace = x[0] + x[1] + r
#            ans.append(LiseNode(inplace % 10))
#            r = inplace / 10
#        return ans.next

#sln = Solution()
#xx = ListNode(2)
#xx.append(ListNode(4)).append(ListNode(3))
#yy = ListNode(5)
#yy.append(ListNode(6)).append(ListNode(4))
#for x in itertools.izip_longest(xx, yy, fillvalue = 0):
#    print x

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        cur = ans
        r = 0
        while l1 or l2 or (r != 0): # important (r != 0)
            inplace = r
            if l1 != None:
                inplace += l1.val             
            if l2 != None:
                inplace += l2.val
            cur.next = ListNode(inplace % 10)
            r = inplace / 10
            if l1 != None:
                l1 = l1.next                          
            if l2 != None:
                l2 = l2.next
            cur = cur.next
        return ans.next

xx = [ListNode(2), ListNode(4), ListNode(3)]
yy = [ListNode(5), ListNode(6), ListNode(4)]
xx[0].next = xx[1]
xx[1].next = xx[2]
yy[0].next = yy[1]
yy[1].next = yy[2]
xx = [ListNode(5)]
yy = [ListNode(5)]
sln = Solution()
ans = sln.addTwoNumbers(xx[0], yy[0])
while ans != None:
    print ans.val
    ans = ans.next
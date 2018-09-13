# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

import Queue
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stk = []
        n = len(nestedList)
        for i in xrange(n-1, -1, -1):
            self.stk.append(nestedList[i])
        self.q = Queue.Queue()

    def next(self):
        """
        :rtype: int
        """
        if not self.q.empty():
            return q.get()
        while 1:
            if len(self.stk) == 0:
                return None
            ni = self.stk.pop()
            if ni.isInteger():
                return ni.getInteger()
            else:
                lst = ni.getList()
                n = len(lst)
                for i in xrange(n-1, -1, -1):
                    self.stk.append(lst[i])

    def hasNext(self):
        """
        :rtype: bool
        """
        nn = self.next()
        if nn == None:
            return False
        else:
            self.q.put(nn)
            return True

# Your NestedIterator object will be instantiated and called as such:
nestedList = []
i, v = NestedIterator(nestedList), []
while i.hasNext(): 
    v.append(i.next())
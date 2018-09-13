n = 0

import Queue

class Ran(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def max_dis(self):
        if self.l == 0:
            # Number of zeros
            return self.r + 1
        elif self.r == n - 1:
            # Number of zeros
            return n - self.l
        else:
            # Number of zeros
            c = self.r - self.l + 1
            return (c + 1) / 2

    def __cmp__(self, other):
        s, o = self.max_dis(), other.max_dis()
        if s == o:
            # Important
            return cmp(self.l, other.r)
        else:
            return -cmp(s, o)


class ExamRoom(object):
    def __init__(self, N):
        """
        :type N: int
        """
        global n
        n = N   
        self.q = Queue.PriorityQueue()
        self.q.put(Ran(0, n - 1))

    def seat(self):
        """
        :rtype: int
        """
        ran = self.q.get()
        l, r = ran.l, ran.r

        if l == 0:
            if l + 1 <= r:
                self.q.put(Ran(l + 1, r))
            return l
        elif r == n - 1:
            if r - 1 >= l:
                self.q.put(Ran(l, r - 1))
            return r

        ll = r - l + 1
        mid = 0
        if ll % 2 == 0:
            mid = (ll - 1) / 2 + l
        else:
            mid = ll / 2 + l

        if mid - 1 >= l:
            self.q.put(Ran(l, mid - 1))
        if mid + 1 <= r:
            self.q.put(Ran(mid + 1, r))

        return mid

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        newq = Queue.PriorityQueue()
        L = None
        R = None
        while not self.q.empty():
            ran = self.q.get()
            l, r = ran.l, ran.r
            if r + 1 == p:
                L = l
            elif l - 1 == p:
                R = r
            else:
                newq.put(ran)
        if L != None and R != None:
            newq.put(Ran(L, R))
        elif L != None:
            newq.put(Ran(L, p))
        elif R != None:
            newq.put(Ran(p, R))
        else:
            # Important
            newq.put(Ran(p, p))

        self.q = newq

# # Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(10)
# p = obj.seat()
# print p, obj.q.qsize()
# # while not obj.q.empty():
# #     ran = obj.q.get()
# #     print ran.l, ran.r  

# obj.leave(p)
# # while not obj.q.empty():
# #     ran = obj.q.get()
# #     print ran.l, ran.r  

# p = obj.seat()
# print p, obj.q.qsize()

# obj = ExamRoom(10)
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.leave(4)
# print obj.seat()
# # 0,9,4,2,null,5

# obj = ExamRoom(4)
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.leave(1)
# print obj.leave(3)
# print obj.seat()
# # 0,9,4,2,null,5

# obj = ExamRoom(10)
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.leave(0)
# print obj.leave(4)
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.seat()
# print obj.leave(0)
# # 0,9,4,null,null,0,4,2,6,1,3,5,7,8,null
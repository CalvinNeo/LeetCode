# coding: utf8
import Queue

global_t = 0
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        global global_t
        inf = 5555555555555
        def can_perform(nxt):
            return global_t >= nxt

        class OK(object):
            def __init__(self, name, cnt):
                self.name = name
                self.cnt = cnt
            def __cmp__(self, other):
                return cmp(-self.cnt, -other.cnt)

        class Wait(object):
            def __init__(self, name, cnt, next):
                self.name = name
                self.cnt = cnt
                self.next = next
            def __cmp__(self, other):
                return cmp(self.next, other.next)

        global_t = 0
        okq = Queue.PriorityQueue()
        waitq = Queue.PriorityQueue()
        d = {}
        for a in tasks:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        for k, v in d.iteritems():
            waitq.put(Wait(k, v, 1))

        while okq.qsize() > 0 or waitq.qsize() > 0:
            global_t += 1
            while waitq.qsize() > 0:
                top = waitq.get()
                if global_t >= top.next:
                    # print "Move To OK {}".format(top.name)
                    okq.put(OK(top.name, top.cnt))
                else:
                    waitq.put(top)
                    break

            if okq.qsize() > 0:
                top = okq.get()
                if top.cnt > 1:
                    # print "Move To Wait {}".format(top.name)
                    waitq.put(Wait(top.name, top.cnt - 1, global_t + n + 1))
            #     print "{} {} {}".format(global_t, top.name, top.cnt - 1)
            # else:
            #     print "{} _".format(global_t)

        return global_t

sln = Solution()
print sln.leastInterval(["A"], 1) # 1
print sln.leastInterval(["A","A","A","B","B","B"], 2) # 8
print sln.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) # 16
print sln.leastInterval(["A","A","A","B","B","B"], 0) # 6

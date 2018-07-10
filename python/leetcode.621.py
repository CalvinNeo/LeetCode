# coding: utf8
import Queue

global_t = 0
class Solution(object):
    def leastIntervalTLE(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        global global_t
        inf = 5555555555555
        def can_perform(nxt):
            return global_t >= nxt

        class Nd(object):
            def __init__(self, task, cnt):
                self.task = task
                self.cnt = cnt
                self.next = 1
            def __cmp__(self, other):
                # print "cmp", self.task, other.task, self.next, other.next
                if self.next == other.next or (can_perform(self.next) and can_perform(other.next)):
                    # 优先返回cnt最大的
                    return cmp(-self.cnt, -other.cnt)
                else:
                    # 优先返回最老的，即next最小
                    return cmp(self.next, other.next)

        global_t = 0
        # pq = Queue.PriorityQueue()
        pq = []
        d = [0] * 26
        for a in tasks:
            d[ord(a) - ord('A')] += 1
        for k, v in enumerate(d):
        #     pq.put(Nd(k, v))
            if v > 0:
                pq.append(Nd(k, v))

        # while pq.qsize() > 0:
        while len(pq) > 0:
            global_t += 1
            pq.sort()
            # top = pq.get()
            top = pq.pop(0)
            if not can_perform(top.next):
                # print global_t, "_"
                # pq.put(top)
                pq.append(top)
            else:
                # print global_t, top.task, "next", global_t + n + 1
                if top.cnt > 1:
                    top.cnt -= 1
                    top.next = global_t + n + 1
                    pq.append(top)
                    # pq.put(top)
        return global_t

    def leastIntervalTLE2(self, tasks, n):
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

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        inf = 5555555555555

        cnt_all = len(tasks)
        d = {}
        for a in tasks:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1

        lst = []
        for k, v in d.iteritems():
            lst.append((k, v))
        lst.sort(key = lambda x: x[1])

        ans = 0
        most = lst[-1][1]
        m = len(lst)
        i = m - 1
        most_cnt = 0
        while i >= 0:
            if lst[i][1] < most:
                break
            most_cnt += 1
            i -= 1
        i += 1
        scaf = cnt_all - most_cnt * most

        need_to_fill = (most - 1) * (n + 1 - most_cnt) - scaf
        # print "cnt_all {}, scaf {}, most {}, most_cnt {}, need_to_fill {}".format(cnt_all, scaf, most, most_cnt, need_to_fill)
        if need_to_fill < 0:
            need_to_fill = 0
        return cnt_all + need_to_fill

sln = Solution()
print sln.leastInterval(["A"], 1) # 1
print sln.leastInterval(["A","A","A","B","B","B"], 2) # 8
print sln.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) # 16
print sln.leastInterval(["A","A","A","B","B","B"], 0) # 6

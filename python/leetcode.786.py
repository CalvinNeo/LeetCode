import Queue
class Solution(object):
    def kthSmallestPrimeFractionTLE(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)
        pq = Queue.PriorityQueue()

        class Nd(object):
            def __init__(self, x, y):
                self.p = x
                self.q = y
            def __cmp__(self, other):
                return cmp(A[self.p] * 1.0 / A[self.q], A[other.p] * 1.0 / A[other.q])

        k = K
        vis = [[0 for i in xrange(n)] for j in xrange(n)]
        def valid(p, q):
            return (0 <= p < n and p < q < n) and not vis[p][q]

        pq.put(Nd(0, n - 1))
        vis[0][n - 1] = 1
        while pq.qsize() > 0:
            node = pq.get()
            p = node.p
            q = node.q
            k -= 1
            # print "p {} q {}".format(p, q)
            if k == 0:
                return [A[p], A[q]]
            if valid(p, q - 1):
                # print "Insert {} {}".format(p, q - 1)
                vis[p][q - 1] = 1
                pq.put(Nd(p, q - 1))
            if valid(p + 1, q):
                # print "Insert {} {}".format(p + 1, q)
                vis[p + 1][q] = 1
                pq.put(Nd(p + 1, q))

    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)
        pq = Queue.PriorityQueue()

        class Nd(object):
            def __init__(self, x, y):
                self.p = x
                self.q = y
            def __cmp__(self, other):
                return cmp(A[self.p] * 1.0 / A[self.q], A[other.p] * 1.0 / A[other.q])

        k = K
        def valid(p, q):
            return (0 <= p < n and p < q < n)
        for i in xrange(n - 1):
            pq.put(Nd(i, n - 1))
        while pq.qsize() > 0:
            node = pq.get()
            p = node.p
            q = node.q
            k -= 1
            # print "p {} q {}".format(p, q)
            if k == 0:
                return [A[p], A[q]]
            if valid(p, q - 1):
                # print "Insert {} {}".format(p, q - 1)
                pq.put(Nd(p, q - 1))
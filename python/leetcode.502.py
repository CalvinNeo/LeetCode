import Queue
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        n = len(Profits)

        qc = Queue.PriorityQueue()
        qp = Queue.PriorityQueue()

        for p, c in zip(Profits, Capital):
            qc.put((c, p))

        for j in xrange(k):
            while not qc.empty():
                c, p = qc.get()
                if c > W:
                    qc.put((c, p))
                    break
                else:
                    qp.put(-p)

            if not qp.empty():
                d = -qp.get()
                W += d
            else:
                break
        return W

# sln = Solution()
# print sln.findMaximizedCapital(k=2, W=0, Profits=[1,2,3], Capital=[0,1,1])
# print sln.findMaximizedCapital(k=2, W=0, Profits=[], Capital=[])
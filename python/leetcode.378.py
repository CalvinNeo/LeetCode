import Queue
class Cell(object):
    def __init__(self, i, x):
        self.i = i
        self.x = x
    def __cmp__(self, other):
        return cmp(self.x, other.x)

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        # mx = max([max(l) for l in matrix])
        # mi = min([min(l) for l in matrix])
        if k > n * m or k <= 0:
            return 0
        pq = Queue.PriorityQueue()
        index = [0] * n
        for i in xrange(n):
            # print "Put", matrix[i][0]
            pq.put(Cell(i, matrix[i][0]))
        while k:
            cell = pq.get()
            i, x = cell.i, cell.x
            # print i, x
            k -= 1
            index[i] += 1
            if index[i] < m:
                # print "Put", matrix[i][index[i]]
                pq.put(Cell(i, matrix[i][index[i]]))
            if k == 0:
                return x

sln = Solution()
print sln.kthSmallest([[ -5]], 1)
print sln.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8)
print sln.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 1)
print sln.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 2)
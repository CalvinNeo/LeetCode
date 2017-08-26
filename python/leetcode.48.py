class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = n - 1
        rev1 = lambda tup: (m - tup[1], m - tup[0])
        rev2 = lambda tup: (m - tup[0], tup[1])
        def sw(fr, to):
            matrix[fr[0]][fr[1]], matrix[to[0]][to[1]] = matrix[to[0]][to[1]], matrix[fr[0]][fr[1]]
        upperTriangle = [(x, y) for x in xrange(m) for y in xrange(m - x)]
        horizon = [(x, y) for x in xrange(n / 2) for y in xrange(n)]
        for tup in upperTriangle:
            sw(tup, rev1(tup))
        for tup in horizon:
            sw(tup, rev2(tup))

sln = Solution()
m = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sln.rotate(m)
print m
class Solution(object):
    def rotate1(self, matrix):
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

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = n - 1
        def gi(i, j):
            return i * n + j

        def gc(i):
            return (i / n, i % n)

        def gx((x, y)):
            return matrix[x][y]

        def move(i, val):
            (x1, y1) = gc(i)
            prev = matrix[x1][y1]
            matrix[x1][y1] = val
            return prev

        def gn(cur):
            (x, y) = gc(cur)
            (x1, y1) = (x - m, y - m)
            (x2, y2) = (y1 + m, -x1)
            next = gi(x2, y2)
            return next

        j = 0
        for i in xrange(n * n):
            cur = i
            flag = False
            new_loop = True
            while True:
                if i == cur:
                    if flag:
                        break
                    else:
                        flag = True
                if cur < i:
                    new_loop = False
                    break
                next = gn(cur)
                cur = next

            if new_loop:
                cur = i
                flag = False
                prev = None
                while True:
                    if i == cur:
                        if flag:
                            prev = move(cur, prev)
                            break
                        else:
                            flag = True
                            next = gn(cur)
                            prev = gx(gc(i))

                    next = gn(cur)
                    # print gc(cur), gc(next)
                    prev = move(cur, prev)
                    cur = next

sln = Solution()
m = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sln.rotate(m)
print m
m = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sln.rotate1(m)
print m
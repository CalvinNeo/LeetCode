class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        row_sum = [[0 for i in xrange(m)] for j in xrange(n)]
        col_sum = [[0 for i in xrange(m)] for j in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                if j == 0:
                    row_sum[i][j] = grid[i][j]
                else:
                    row_sum[i][j] = grid[i][j] + row_sum[i][j - 1]
        

        for j in xrange(m):
            for i in xrange(n):
                if i == 0:
                    col_sum[i][j] = grid[i][j]
                else:
                    col_sum[i][j] = grid[i][j] + col_sum[i - 1][j]

        def valid(x, y, l):
            s = None
            # print "x {} y {}".format(x, y)

            for i in xrange(x, x + l):
                ss = 0
                if y == 0:
                    ss = row_sum[i][y+l-1]
                else:
                    ss = row_sum[i][y+l-1] - row_sum[i][y-1]
                if s == None:
                    s = ss
                elif s != ss:
                    return False

            for i in xrange(y, y + l):
                ss = 0
                if x == 0:
                    ss = col_sum[x+l-1][i]
                else:
                    ss = col_sum[x+l-1][i] - row_sum[x-1][i]
                if s == None:
                    s = ss
                elif s != ss:
                    return False

            ss = 0
            for i in xrange(0, l):
                ss += grid[x+i][y+i]
            if s == None:
                s = ss
            elif ss != s:
                return False

            ss = 0
            for i in xrange(0, l):
                ss += grid[x+i][y+l-1-i]
            if s == None:
                s = ss
            elif ss != s:
                return False

            return True

        ans = 0
        for i in xrange(n - 2):
            for j in xrange(m - 2):
                if valid(i, j, 3):
                    ans += 1
                # print "========================"
        return ans

sln = Solution()
# print sln.numMagicSquaresInside([[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]) # 1
print sln.numMagicSquaresInside([[10,3,5],[1,6,11],[7,9,2]]) # 1

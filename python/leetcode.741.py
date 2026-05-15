def pg(g):
    for l in g:
        print " ".join(map(str, l))
    print "====="

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == -1:
            return 0
        dp = [[[0 for k in xrange(n+3)] for i in xrange(n+3)] for j in xrange(n+3)]
        acc = [[0 for i in xrange(n+2)] for j in xrange(n+2)]

        acc[0][0] = 1
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == -1:
                    acc[i][j] = 0
                    continue
                if i-1 >= 0 and grid[i-1][j] != -1:
                    acc[i][j] |= acc[i-1][j]
                if j-1 >= 0 and grid[i][j-1] != -1:
                    acc[i][j] |= acc[i][j-1]

        for x1 in xrange(n):
            for y1 in xrange(n):
                for x2 in xrange(n):
                    y2 = x1 + y1 - x2

                    # print "Z [{},{}] and [{},{}] acc p1 {} p2 {}".format(x1, y1, x2, y2, acc[x1][y1], acc[x2][y2])
                    if y2 < 0 or y2 >= n:
                        continue
                    if (not acc[x1][y1]) or (not acc[x2][y2]):
                        continue

                    assert dp[x1][y1][x2] == 0
                    if x1 == x2 and y1 == y2:
                        dp[x1][y1][x2] += grid[x1][y1]
                    else:
                        dp[x1][y1][x2] += grid[x1][y1]
                        dp[x1][y1][x2] += grid[x2][y2]

                    choices = [
                        dp[x1-1][y1][x2],
                        dp[x1][y1-1][x2],
                        dp[x1-1][y1][x2-1],
                        dp[x1][y1-1][x2-1],
                    ]

                    mc = max(choices)

                    # print "[{},{}] and [{},{}] by cell {} by dp {}".format(x1, y1, x2, y2, dp[x1][y1][x2], mc)
                    dp[x1][y1][x2] += mc

        return dp[n-1][n-1][n-1]


    def cherryPickupWAGreedy(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == -1:
            return 0
        dp = [[0 for i in xrange(n+2)] for j in xrange(n+2)]
        acc = [[0 for i in xrange(n+2)] for j in xrange(n+2)]

        pg(grid)
        acc[0][0] = 1
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == -1:
                    acc[i][j] = 0
                    continue
                if i-1 >= 0 and grid[i-1][j] != -1:
                    acc[i][j] |= acc[i-1][j]
                if j-1 >= 0 and grid[i][j-1] != -1:
                    acc[i][j] |= acc[i][j-1]

        for i in xrange(n):
            for j in xrange(n):
                if not acc[i][j]:
                    continue
                if grid[i][j] == 1:
                    dp[i][j] = 1
                C = []
                # print "c i {} j {}".format(i, j)
                if i-1 >= 0 and acc[i-1][j]:
                    C.append(dp[i-1][j])
                if j-1 >= 0 and acc[i][j-1]:
                    C.append(dp[i][j-1])
                if C:
                    dp[i][j] += max(C)

        if dp[n-1][n-1] == 0:
            return 0

        ans = dp[n-1][n-1]
        # print "part ans {}".format(ans)

        pg(grid)
        i = n - 1
        j = n - 1
        while i or j:
            t = grid[i][j]
            x = dp[i][j] - t
            grid[i][j] = 0
            if i >= 1 and x == dp[i-1][j]:
                # print "({},{}) -> ({},{})".format(i-1,j,i,j)
                i -= 1
            if j >= 1 and x == dp[i][j-1]:
                # print "({},{}) -> ({},{})".format(i,j-1,i,j)
                j -= 1
        grid[0][0] = 0
        # print "sweep {}".format(grid)

        dp = [[0 for i in xrange(n+2)] for j in xrange(n+2)]
        for i in xrange(n):
            for j in xrange(n):
                if not acc[i][j]:
                    continue
                if grid[i][j] == 1:
                    dp[i][j] = 1
                C = []
                if i-1 >= 0 and acc[i-1][j]:
                    C.append(dp[i-1][j])
                if j-1 >= 0 and acc[i][j-1]:
                    C.append(dp[i][j-1])
                if C:
                    dp[i][j] += max(C)

        return ans + dp[n-1][n-1]

sln = Solution()
print sln.cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]) # 5
print sln.cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]) # 0
print sln.cherryPickup([[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]) # 15

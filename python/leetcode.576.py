MOD = 10 ** 9 + 7
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0 for y in xrange(n + 2)] for x in xrange(m + 2)] for k in xrange(N + 1)]
        DX = [-1, 0, 0, 1]
        DY = [0, -1, 1, 0]

        def inb(x, y):
            return 1 <= x <= m and 1 <= y <= n
        def onb(x, y):
            return (x in [0, m + 1] and 1 <= y <= n) or (y in [0, n + 1] and 1 <= x <= m)
        def valid(x):
            return inb(x, y) or onb(x, y)

        i += 1
        j += 1

        dp[0][i][j] = 1

        ans = 0
        for k in xrange(1, N + 1):
            for x in xrange(m + 2):
                for y in xrange(n + 2):
                    for dx, dy in zip(DX, DY):
                        if inb(x + dx, y + dy):
                            # print "dp[{}][{}][{}] = {}".format(k - 1, x + dx, y + dy, dp[n - 1][x + dx][y + dy])
                            dp[k][x][y] += dp[k - 1][x + dx][y + dy]
                            dp[k][x][y] %= MOD
                        # if onb(x + dx, y + dy):
                        #     ans += dp[k - 1][x + dx][y + dy]
                        #     ans %= MOD
        ans = 0
        for k in xrange(1, N + 1):
            for x in [0, m + 1]:
                for y in xrange(1, n + 1):
                    ans += dp[k][x][y]
                    ans %= MOD

            for y in [0, n + 1]:
                for x in xrange(1, m + 1):
                    ans += dp[k][x][y]
                    ans %= MOD

        return ans

sln = Solution()
print sln.findPaths(2,2,2,0,0)
print sln.findPaths(1,3,3,0,1)
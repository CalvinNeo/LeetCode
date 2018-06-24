class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        DX = [-2, -1, +1, +2, +2, +1, -1, -2]
        DY = [-1, -2, -2, -1, +1, +2, +2, +1]
        def out(x, y):
            return x < 0 or x >= N or y < 0 or y >= N
        dp = [[[0 for i in xrange(N)] for j in xrange(N)] for k in xrange(K + 1)]
        for i in xrange(N):
            for j in xrange(N):
                dp[0][i][j] = 0.0
        dp[0][r][c] = 1.0
        for k in xrange(1, K + 1):
            for i in xrange(N):
                for j in xrange(N):
                    for (dx, dy) in zip(DX, DY):
                        pi, pj = i - dx, j - dy
                        if out(pi, pj):
                            dp[k][i][j] += 0
                        else:
                            dp[k][i][j] += dp[k - 1][pi][pj] / 8.0
        # print dp
        return sum(map(sum, dp[K]))
sln = Solution()
print sln.knightProbability(3, 2, 0, 0)
# 1 0 0
# 0 0 0
# 0 0 0
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])

        dp = [[0 for j in xrange(m)] for i in xrange(n)]
        DX = [-1, 0, 0, 1]
        DY = [0, -1, 1, 0]
        def valid(x, y):
            return (0 <= x < n) and (0 <= y < m)

        def dfs(x, y):
            for (dx, dy) in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    if matrix[nx][ny] < matrix[x][y]:
                        if dp[nx][ny] == 0:
                            dfs(nx, ny)
                        dp[x][y] = max(dp[nx][ny] + 1, dp[x][y])
            if dp[x][y] == 0:
                dp[x][y] = 1

        for i in xrange(n):
            for j in xrange(m):
                dfs(i, j)

        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                ans = max(ans, dp[i][j])
        # print dp
        return ans

sln = Solution()
print sln.longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
])
print sln.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
] )
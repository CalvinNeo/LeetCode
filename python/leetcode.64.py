class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid) 
        n = len(grid[0])
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in xrange(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+ grid[i][j]
        return dp[m-1][n-1]

sln = Solution()
print sln.minPathSum([[1]])
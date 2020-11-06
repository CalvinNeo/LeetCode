class Solution(object):
    def minFallingPathSumWA(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])


        inf = 55555555555555555
        dp = [[0 for i in xrange(m + 1)] for j in xrange(n + 1)]

        dp[0][0] = A[0][0]

        for i in xrange(n):
            for j in xrange(m):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = min([dp[i - 1][j], dp[i][j - 1]]) + A[i][j]

        return dp[n - 1][m - 1]

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])


        inf = 55555555555555555
        dp = [[inf for i in xrange(m + 2)] for j in xrange(n + 2)]

        for j in xrange(m):
            dp[0][j] = A[0][j]

        for i in xrange(1, n):
            for j in xrange(m):
                dp[i][j] = min([dp[i - 1][j + 1], dp[i - 1][j], dp[i - 1][j - 1]]) + A[i][j]

        # print dp
        return min(dp[n - 1])

sln = Solution()
print sln.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) # 12
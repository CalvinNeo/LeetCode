class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        m = len(mat)
        n = len(mat[0])

        cumu = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]

        for i in xrange(m):
            for j in xrange(n):
                cumu[i][j] = cumu[i][j - 1] + mat[i][j]

        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]

        for i in xrange(m):
            for j in xrange(n):
                dp[i][j] = dp[i - 1][j] + cumu[i][j]

        ans = [[0 for j in xrange(n)] for i in xrange(m)]

        def compute(i, j):
            i0 = max(i - K, 0)
            i1 = min(i + K, m - 1)
            j0 = max(j - K, 0)
            j1 = min(j + K, n - 1)
            # print "x {} y {} l {} r {} t {} b {}".format(x, y, l, r, t, b)
            i_bar = 0
            if i0 - 1 >= 0:
                i_bar = dp[i0 - 1][j1]
            ij_bar = 0
            if i0 - 1 >= 0 and j0 - 1 >= 0:
                ij_bar = dp[i0 - 1][j0 - 1]
            j_bar = 0
            if j0 - 1 >= 0:
                j_bar = dp[i1][j0 - 1]
            major_bar = dp[i1][j1]
            # print "x {} y {} top_bar {} left_bar {} top_left_bar {}".format(x, y, top_bar, left_bar, top_left_bar)
            return major_bar - i_bar - j_bar + ij_bar

        for i in xrange(m):
            for j in xrange(n):
                ans[i][j] = compute(i, j)

        # print dp
        return ans

sln = Solution()
print sln.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1)
# [[12,21,16],[27,45,33],[24,39,28]]
print sln.matrixBlockSum([[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]], 3)
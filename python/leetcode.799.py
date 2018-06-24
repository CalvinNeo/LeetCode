class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0 for j in xrange(query_row + 2)] for i in xrange(query_row + 2)]

        dp[0][0] = poured
        for i in xrange(query_row + 1):
            for j in xrange(query_row + 1):
                if dp[i][j] > 1.0:
                    dp[i + 1][j] += (dp[i][j] - 1.0) / 2.0
                    dp[i + 1][j + 1] += (dp[i][j] - 1.0) / 2.0
                    dp[i][j] = 1.0
        return dp[query_row][query_glass]
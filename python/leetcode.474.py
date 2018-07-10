class Solution(object):
    def findMaxFormTLE(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ll = len(strs)
        dp = [[[0 for k in xrange(n + 1)] for j in xrange(m + 1)] for i in xrange(ll + 1)]

        for i in xrange(1, ll + 1):
            for j in xrange(m + 1):
                for k in xrange(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    zs = len(filter(lambda x: x == '0', strs[i - 1]))
                    os = len(filter(lambda x: x == '1', strs[i - 1]))
                    if j - zs >= 0 and k - os >= 0:
                        dp[i][j][k] = max(dp[i][j][k], 1 + dp[i - 1][j - zs][k - os])
        return dp[ll][m][n]

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ll = len(strs)
        dp = [[0 for k in xrange(n + 1)] for j in xrange(m + 1)]
        zeros = [len(filter(lambda x: x == '0', s)) for s in strs]
        ones = [len(filter(lambda x: x == '1', s)) for s in strs]
        for i in xrange(1, ll + 1):
            for j in xrange(m, -1, -1):
                for k in xrange(n, -1, -1):
                    zs = zeros[i - 1]
                    os = ones[i - 1]
                    if j - zs >= 0 and k - os >= 0:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - zs][k - os])
        return dp[m][n]
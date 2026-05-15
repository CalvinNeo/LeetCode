class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        S = [[0 for i in xrange(k+2)] for j in xrange(n+2)]
        M = 10**9 + 7

        for i in xrange(n+1):
            S[i][-1] = 0
        for i in xrange(n+1):
            S[i][0] = 1
        for i in xrange(k+1):
            S[1][i] = 1

        for i in xrange(2, n+1):
            for j in xrange(1, k+1):
                f = max(j - i, -1)
                x = S[i-1][j] - S[i-1][f]
                # print "delta i {} j {} f {} S[i-1][j] {} S[i-1][f] {} res = {}".format(i, j, f, S[i-1][j], S[i-1][f], x)
                S[i][j] = (S[i][j-1] + x) % M

        # print S
        return (S[n][k] - S[n][k-1]) % M


    def kInversePairsTLE(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        M = 10e9 + 7
        dp = [[0 for i in xrange(k+1)] for j in xrange(n+1)]

        for i in xrange(n+1):
            dp[i][0] = 1

        for i in xrange(2, n+1):
            for j in xrange(1, k+1):
                f = max(j - (i - 1), 0)
                t = j
                dp[i][j] = sum(dp[i-1][f:t+1]) % M

        return dp[n][k]

    def kInversePairsWA(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0 for i in xrange(k+1)] for j in xrange(n+1)]

        dp[1][0] = 1
        for i in xrange(n+1):
            dp[i][0] = 1

        for i in xrange(2, n+1):
            for j in xrange(1, k+1):
                f = max(k - (n - 1), 0)
                t = k
                # print "i {} j {} t {} dp[i-1] {}".format(i, j, t, dp[i-1])
                dp[i][j] = sum(dp[i-1][f:t+1])

        print dp
        return dp[n][k]

sln = Solution()
print sln.kInversePairs(3, 0) # 1
print sln.kInversePairs(3, 1) # 2
print sln.kInversePairs(3, 1) # 2
print sln.kInversePairs(2, 2) # 0
print sln.kInversePairs(3, 2) # 2
print sln.kInversePairs(1000, 1000) # 663677020
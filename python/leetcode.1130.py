class Solution(object):
    def mctFromLeafValuesWA(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[5555555555 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n):
            dp[i][i] = 0

        for i in xrange(n - 1):
            dp[i][i+1] = arr[i] * arr[i + 1]

        for i in xrange(n):
            for j in xrange(i + 2, n):
                for k in xrange(i, j):
                    # [i..k], [k+1..j]
                    delta = dp[i][k] + dp[k+1][j] + max(arr[i:k+1]) * max(arr[k+1:j+1])
                    print "i {} j {} k {} = {}, dp[i][k]={} dp[k+1][j]={}, max {} {}".format(i, j, k, delta, dp[i][k], dp[k+1][j], max(arr[i:k+1]), max(arr[k:j+1]))
                    dp[i][j] = min(dp[i][j], delta)

        return dp[0][n-1]

    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[5555555555 for j in xrange(n)] for i in xrange(n)]
        mx = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n):
            mx[i][i] = arr[i]
            for j in xrange(i + 1, n):
                mx[i][j] = max(mx[i][j - 1], arr[j])

        for i in xrange(n):
            dp[i][i] = 0

        for i in xrange(n - 1):
            dp[i][i+1] = arr[i] * arr[i + 1]

        for l in xrange(2, n + 1):
            for i in xrange(0, n - l + 1):
                j = i + l - 1
                for k in xrange(i, j):
                    # [i..k], [k+1..j]
                    delta = dp[i][k] + dp[k+1][j] + mx[i][k] * mx[k+1][j]
                    # print "i {} j {} k {} = {}, dp[i][k]={} dp[k+1][j]={}, max {} {}".format(i, j, k, delta, dp[i][k], dp[k+1][j], mx[i][k], mx[k+1][j])
                    dp[i][j] = min(dp[i][j], delta)

        return dp[0][n-1]

sln = Solution()
print sln.mctFromLeafValues([6,2]) # 12
print sln.mctFromLeafValues([6,2,4]) # 32
print sln.mctFromLeafValues([15,13,5,3,15]) # 500
print sln.mctFromLeafValues([ 8,7,10,12]) # 256
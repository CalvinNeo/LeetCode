class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        inf = 555555555
        dp = [[inf for i in xrange(n)] for j in xrange(n)]
        def valid(i):
            return 0 <= i < n
        def update(fr, to, v):
            # print "Try Update [{}, {}] to {}".format(fr, to, v)
            dp[fr][to] = min(dp[fr][to], v)
        if n == 0:
            return 0
        for i in xrange(n):
            dp[i][i] = 1
        for i in xrange(n - 1):
            dp[i][i + 1] = 1 if s[i] == s[i + 1] else 2
        for step in xrange(2, n):
            for fr in xrange(n - step):
                to = fr + step
                for k in xrange(fr, to):
                    if s[k] == s[to]:
                        update(fr, to, dp[fr][k] + dp[k + 1][to] - 1) 
                    else:
                        update(fr, to, dp[fr][k] + dp[k + 1][to]) 
        return dp[0][n - 1]
        
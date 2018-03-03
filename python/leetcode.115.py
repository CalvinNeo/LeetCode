class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def merge_str(ss):
            lst = [[None, 1]]
            for ch in ss:
                if lst[-1][0]  == ch:
                    lst[-1][1] += 1
                else:
                    lst.append([ch, 1])
            lst = lst[1:]

        m = len(s)
        n = len(t)
        import sys
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = 1
        for i in xrange(1, m + 1):
            dp[i][0] = 1
        for j in xrange(1, n + 1):
            dp[0][j] = 0
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]
sln = Solution()
print sln.numDistinct("rabbbit", "rabbit")
print sln.numDistinct("rrr", "r")
print sln.numDistinct("r", "rrr")
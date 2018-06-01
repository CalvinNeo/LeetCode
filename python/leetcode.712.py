class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n1 = len(s1)
        n2 = len(s2)
        inf = 10000000000
        dp = [[inf for i in xrange(n2 + 1)] for j in xrange(n1 + 1)]
        dp[0][0] = 0
        # Initialize not forget, important!!
        for i in xrange(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in xrange(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in xrange(1, n1 + 1):
            for j in xrange(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = inf

                ch1 = dp[i][j - 1] + ord(s2[j - 1]) # delete s2
                ch2 = dp[i - 1][j] + ord(s1[i - 1]) # delete s1
                if ch1 > ch2:
                    # delete s1, choose ch2
                    dp[i][j] = min(dp[i][j], ch2)
                    # print "At ({} {}), choose delete s1 {} at cost {}, final {}".format(i, j, s1[i - 1], ch2, dp[i][j])
                else:
                    # delete s2
                    dp[i][j] = min(dp[i][j], ch1)
                    # print "At ({} {}), choose delete s2 {} at cost {}, final {}".format(i, j, s2[j - 1], ch1, dp[i][j])

        return dp[n1][n2]

sln = Solution()
print sln.minimumDeleteSum("sea", "eat")
print sln.minimumDeleteSum("delete", "leet")
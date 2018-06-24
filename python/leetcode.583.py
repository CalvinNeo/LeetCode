class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0 for i in xrange(n2 + 1)] for j in xrange(n1 + 1)]

        for i in xrange(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1

        for i in xrange(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1


        for i in xrange(1, n1 + 1):
            for j in xrange(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[n1][n2]

sln = Solution()
print sln.minDistance("sea", "eat")
print sln.minDistance("abc", "abb")
print sln.minDistance("abc", "ab")
print sln.minDistance("abc", "")
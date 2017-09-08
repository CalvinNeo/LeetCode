class Solution1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) 
        n = len(word2)
        import sys
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        for i in xrange(0, m):
            for j in xrange(0, n):
                if word1[i] != word2[j]:
                    dp[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        # print "1", dp[i-1][j-1]
                        dp[i][j] = dp[i-1][j-1]
                    if i - 1 >= 0:
                        # print "2", dp[i-1][j]
                        dp[i][j] = min(dp[i][j], dp[i-1][j])
                    elif j - 1 >= 0:
                        # print "3", dp[i][j-1]
                        dp[i][j] = min(dp[i][j], dp[i][j-1])
                    # print "i,j", i, j, dp[i][j]
                    dp[i][j] += 1
                print "dp[%d][%d] = %d" % (i, j, dp[i][j])
        # print dp
        return dp[m-1][n-1]

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) 
        n = len(word2)
        import sys
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        for i in xrange(m + 1):
            dp[i][0] = i
        for j in xrange(n + 1):
            dp[0][j] = j
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
                # print "dp[%d][%d] = %d" % (i, j, dp[i][j])
        # print dp
        return dp[m][n]

sln = Solution()
print sln.minDistance("abab", "ab")
print sln.minDistance("a", "ab")
print sln.minDistance("c", "ab")

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for i in xrange(l2 + 1)] for i in xrange(l1 + 1)]
        choice = [[0 for i in xrange(l2 + 1)] for i in xrange(l1 + 1)]
        for i in xrange(l1):
            dp[i][0] = 0
            choice[i][0] = 0
        for j in xrange(l2):
            dp[0][j] = 0
            choice[0][j] = 0

        for i in xrange(1, l1 + 1):
            for j in xrange(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    chs = zip([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1], [1,2,3])
                    best = max(chs, key = lambda x: x[0])
                    dp[i][j] = best[0]
                    choice[i][j] = best[1]
                else:
                    chs = zip([dp[i - 1][j], dp[i][j - 1]], [1,2])
                    best = max(chs, key = lambda x: x[0])
                    dp[i][j] = best[0]
                    choice[i][j] = best[1]

        ans = ""
        ii = l1
        jj = l2
        while ii != 0 and jj != 0:
            bc = choice[ii][jj]
            if bc == 1:
                ii -= 1
            elif bc == 2:
                jj -= 1
            else:
                ans = text1[ii - 1] + ans
                ii -= 1
                jj -= 1
        return len(ans)
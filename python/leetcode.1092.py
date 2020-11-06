#coding:utf8

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
        return ans

    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        [l1, l2] = map(len, [str1, str2])
        dp = [[0 for j in xrange(l2 + 1)] for i in xrange(l1 + 1)]
        # 可以把delta插入到LCS中
        lcs = self.longestCommonSubsequence(str1, str2)
        ans = ""
        ii = 0
        jj = 0
        for c in lcs:
            while ii < l1 and str1[ii] != c:
                ans += str1[ii]
                ii += 1
            while jj < l2 and str2[jj] != c:
                ans += str2[jj]
                jj += 1
            ans += c
            ii += 1
            jj += 1
        while ii < l1:
            ans += str1[ii]
            ii += 1
        while jj < l2:
            ans += str2[jj]
            jj += 1
        return ans
            # Now str1/str2 ends or str1/str2 == c
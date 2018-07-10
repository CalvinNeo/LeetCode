class Solution(object):
    def longestPalindromeSubseqWA(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2 if s[0] == s[1] else 1

        dp = [[0 for i in xrange(n )] for j in xrange(n )]

        flag = 0
        for i in xrange(1, n):
            if s[i] == s[0]:
                flag = 1
            if flag:
                dp[0][i] = 2
        flag = 0
        for j in xrange(n - 2, -1, -1):
            if s[j] == s[n - 1]:
                flag = 1
            if flag:
                dp[j][n - 1] = 2

        for i in xrange(n):
            for j in xrange(n - 1, i, -1):
                # print "check [0,{}] and [{},{}]".format(i, j, n - 1)
                if s[i] == s[j] and i - 1 >= 0 and j + 1 < n:
                    dp[i][j] = max(dp[i - 1][j + 1] + 2, dp[i][j])
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1])
        # for d in dp:
        #     print d
        ans = 0
        for i in xrange(n - 1):
            if i + 2 < n:
                ans = max(dp[i][i + 2] + 1, ans)
            ans = max(dp[i][i + 1], ans)
        return ans

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2 if s[0] == s[1] else 1

        dp = [[0 for i in xrange(n )] for j in xrange(n )]

        flag = 0
        for i in xrange(n - 1):
            if s[i] == s[n - 1]:
                flag = 1
            if flag:
                dp[i][n - 1] = 2
        flag = 0
        for j in xrange(n - 2, 0, -1):
            if s[j] == s[0]:
                flag = 1
            if flag:
                dp[0][j] = 2

        for i in xrange(n):
            for j in xrange(n - 1, i, -1):
                # print "check [0,{}] and [{},{}]".format(i, j, n - 1)
                if s[i] == s[j] and i - 1 >= 0 and j + 1 < n:
                    dp[i][j] = max(dp[i - 1][j + 1] + 2, dp[i][j])
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j + 1 < n:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1])
        # for d in dp:
        #     print d
        ans = 0
        for i in xrange(n - 1):
            if i + 2 < n:
                ans = max(dp[i][i + 2] + 1, ans)
            ans = max(dp[i][i + 1], ans)
        return ans

# sln = Solution()
# print sln.longestPalindromeSubseq("bbbab") # 4
# print sln.longestPalindromeSubseq("cbbd") # 2
# print sln.longestPalindromeSubseq("abcba") # 5
# print sln.longestPalindromeSubseq("a") # 1
# print sln.longestPalindromeSubseq("aa") # 2
# print sln.longestPalindromeSubseq("ab") # 1
# print sln.longestPalindromeSubseq("abcabc") # 3
# print sln.longestPalindromeSubseq("abcabcabc") # 5
# print sln.longestPalindromeSubseq("abcabcabcabc") # 7
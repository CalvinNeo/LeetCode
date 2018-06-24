class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        m = len(B)
        dp = [[0 for i in xrange(m + 1)] for j in xrange(n + 1)]


        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    # dp[i][j] = max([dp[i - 1][j - 1] + 1, dp[i - i][j], dp[i][j - 1]])
                    dp[i][j] = dp[i - 1][j - 1] + 1

        ans = 0
        for i in xrange(n + 1):
            for j in xrange(m + 1):
                ans = max(ans, dp[i][j])
        # for l in dp:
        #     print l
        return ans


sln = Solution()
print sln.findLength([1,2,3,2,1], [3,2,1,4,7]) # 3
print sln.findLength([0,1,1,1,1], [1,0,1,0,1]) # 2
print sln.findLength([1,0,0,0,1,0,0,1,0,0], [0,1,1,1,0,1,1,1,0,0]) # 3
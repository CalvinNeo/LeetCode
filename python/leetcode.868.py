class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        n = len(s)
        dp = [-1 for i in xrange(n)]
        for i in xrange(n - 2, -1, -1):
            if s[i + 1] == '1':
                dp[i] = i + 1
            else:
                dp[i] = dp[i + 1]
        ans = 0
        for i in xrange(n):
            if dp[i] != -1:
                ans = max(ans, dp[i] - i)
        # print dp
        return ans

sln = Solution()
print sln.binaryGap(22)
print sln.binaryGap(5)
print sln.binaryGap(6)
print sln.binaryGap(8)
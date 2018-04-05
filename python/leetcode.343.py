dp = [-1] * 100
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

dp2 = [-1] * 100
dp2[0] = 0
dp2[1] = 1
dp2[2] = 1
dp2[3] = 2

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs2(k):
            if dp[k] != -1:
                return dp[k]
            m = 0
            for i in xrange(2, k):
                m = max(m, i * dfs2(k - i))
            dp[k] = m
            return m

        def dfs(k, deep):
            if deep == 0:
                if dp2[k] != -1:
                    return dp2[k]
            else:
                if dp[k] == -1:
                    dfs2(60)
                return dp[k]
            m = 0
            for i in xrange(2, k):
                m = max(m, i * dfs(k - i, deep + 1))
            dp2[k] = m
            return m

        return dfs(n, 0)

sln = Solution()
print sln.integerBreak(3)
print sln.integerBreak(6)
print sln.integerBreak(10)
print sln.integerBreak(20)
print sln.integerBreak(50)
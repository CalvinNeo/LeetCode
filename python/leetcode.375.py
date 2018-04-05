maxn = 1000
dp = [[-1 for i in xrange(maxn)] for j in xrange(maxn)]
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        inf = 5555555555
        def dfs(fr, to):
            if fr >= to:
                return 0
            m = inf
            if fr < maxn and to < maxn and dp[fr][to] != -1:
                return dp[fr][to]
            for mid in xrange(fr, to + 1):
                left = dfs(fr, mid - 1)
                right = dfs(mid + 1, to)
                m = min(m, max(left, right) + mid)
            if fr < maxn and to < maxn:
                dp[fr][to] = m
            return m

        return dfs(1, n)

sln = Solution()
print sln.getMoneyAmount(1)
print sln.getMoneyAmount(2)
print sln.getMoneyAmount(3)
print sln.getMoneyAmount(4)
print sln.getMoneyAmount(10)
print sln.getMoneyAmount(15)
print sln.getMoneyAmount(20)
print sln.getMoneyAmount(30)
print sln.getMoneyAmount(100)
print sln.getMoneyAmount(300)

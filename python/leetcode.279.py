
maxn = 50000
dp = [-1] * maxn
dp[0] = 0

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(cur):
            if cur < maxn and dp[cur] != -1:
                return dp[cur]

            sq = int(cur ** 0.5)
            ans = -1
            for i in xrange(sq, 0, -1):
                t = 1 + dfs(cur - i * i)
                if ans == -1:
                    ans = t
                else:
                    ans = min(ans, t)
            if cur < maxn:
                dp[cur] = ans
            return ans

        return dfs(n)

sln = Solution()
# 0 1 2 3 1 3 2 3 2
print sln.numSquares(0)
print sln.numSquares(1)
print sln.numSquares(2)
print sln.numSquares(3)
print sln.numSquares(4)
print sln.numSquares(6)
print sln.numSquares(8)
print sln.numSquares(12)
print sln.numSquares(13)
x = 1
for i in xrange(1, 7000):
    x +=  sln.numSquares(i)
print x

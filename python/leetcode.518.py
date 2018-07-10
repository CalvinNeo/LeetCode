class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        coins.sort()

        dp = [[0 for k in xrange(n + 1)] for i in xrange(amount + 1)]
        for k in xrange(n + 1):
            dp[0][k] = 1
        for i in xrange(1, amount + 1):
            for k in xrange(1, n + 1):
                if i - coins[k - 1] >= 0:
                    dp[i][k] += dp[i - coins[k - 1]][k]
                if k - 1 >= 0:
                    dp[i][k] += dp[i][k - 1]
        # print dp
        return dp[amount][n]
sln = Solution()
print sln.change(5, [])
print sln.change(5, [1, 2, 5])
print sln.change(3, [2])
print sln.change(10, [10])
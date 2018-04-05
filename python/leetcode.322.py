class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = 555555555
        def pack1():
            n = len(coins)
            dp = [[inf for i in xrange(amount + 1)] for j in xrange(n + 1)]
            dp[0][0] = 0
            for i in xrange(1, n + 1):
                for j in xrange(amount + 1):
                    if j - coins[i - 1] >= 0:
                        dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
                    else:
                        dp[i][j] = dp[i - 1][j]
            if dp[n][amount] == inf:
                return -1
            return dp[n][amount]

        def pack():
            n = len(coins)
            dp = [inf for i in xrange(amount + 1)]
            dp[0] = 0
            for i in xrange(1, n + 1):
                for j in xrange(amount + 1):
                    if j - coins[i - 1] >= 0:
                        dp[j] = min(dp[j - coins[i - 1]] + 1, dp[j])
                    else:
                        dp[j] = dp[j]
            if dp[amount] == inf:
                return -1
            return dp[amount]
        
        return pack()

sln = Solution()
print sln.coinChange([1, 2, 5], 11)
print sln.coinChange([2], 3)
print sln.coinChange([2147483647], 2)
print sln.coinChange([253,27,214,340,158,92,52,126,466,431,95], 3046)

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0

        maxsize = (n + 1) / 2 + 1
        sell = [0 for j in xrange(n + 1)]
        buy = [-55555555555555 for j in xrange(n + 1)]

        for i in xrange(1, n + 1): # at day i
            buy[i] = max( buy[i - 1], sell[i - 1] - prices[i - 1] )

            sell[i] = max( sell[i - 1], buy[i] + prices[i - 1] - fee)

        return sell[n]

sln = Solution()
# 8 6
print sln.maxProfit([1,3,2,8,4,9], 2)
print sln.maxProfit([1,3,7,5,10,3], 3)
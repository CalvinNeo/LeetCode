class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        sell = [0] * (n + 1)
        buy = [0] * (n + 1)
        buy[1] = -prices[0]
        for i in xrange(2, n + 1):
            sell[i] = max(buy[i - 1] + prices[i - 1], sell[i - 1])
            buy[i] = max(sell[i - 2] - prices[i - 1], buy[i - 1])
        m = 0
        for i in xrange(1, n + 1):
            m = max(sell[i], m)
        return m

sln = Solution()
print sln.maxProfit([1, 2, 3, 0, 2])
print sln.maxProfit([])
print sln.maxProfit([1])
print sln.maxProfit([1, 2])
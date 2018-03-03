class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        hold = prices[0]
        prof = 0
        for i in xrange(1, len(prices)):
            if prices[i] > hold:
                prof += (prices[i] - hold)
                hold = prices[i]
            else:
                # important
                hold = prices[i]
        return prof

sln = Solution()
print sln.maxProfit([1,2,3,4,5])

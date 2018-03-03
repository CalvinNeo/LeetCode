class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        import sys
        minl, maxdelta = sys.maxint, 0
        for i in xrange(length):
            minl = min(minl, prices[i])
            maxdelta = max(prices[i]-minl, maxdelta)
        return maxdelta

sln = Solution()
print sln.maxProfit([7, 1, 5, 3, 6, 4])
print sln.maxProfit([7, 6, 4, 3, 1])
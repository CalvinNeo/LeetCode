class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        max_to = [0] * length
        max_since = [0] * length
        current_min = [int(prices[0])] * length
        current_max = [int(prices[-1])] * length
        for i in xrange(1, length):
            current_min[i] = min(current_min[i - 1], prices[i])
        for i in xrange(length-2, -1,-1):
            current_max[i] = max(current_max[i + 1], prices[i])
        for i in xrange(1, length):
            max_to[i] = max(prices[i] - current_min[i], max_to[i-1])
        for i in xrange(length-2,-1,-1):
            max_since[i] = max(current_max[i] - prices[i], max_since[i+1])

        # print max_to
        # print max_since
        res = 0
        for i in xrange(0, length-1):
            res = max(res, max_to[i] + max_since[i])

        return res

sln = Solution()
# print sln.maxProfit([1])
# print sln.maxProfit([1,2])
# print sln.maxProfit([1,2,3])
# print sln.maxProfit([1,2,3,4])
print sln.maxProfit([2,1,2,0,1])

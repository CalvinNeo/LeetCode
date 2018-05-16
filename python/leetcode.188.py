class Solution(object):
    def maxProfitError(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        start = 0
        ss = []
        for i in xrange(n - 1):
            if prices[i + 1] <= prices[i]:
               ss.append((start, i, prices[i] - prices[start])) 
               start = i + 1
        if start != n - 1:
               ss.append((start, n - 1, prices[n - 1] - prices[start])) 

        ss.sort(lambda x, y: x[2] - y[2])
        mm = min(k, len(ss))
        ans = 0
        print ss, mm
        for i in xrange(mm):
            ans += ss[len(ss) - 1 - i][2]
        return ans

    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        start = 0
        ss = []
        for i in xrange(n - 1):
            if prices[i + 1] <= prices[i]:
               ss.append((prices[start], prices[i])) 
               start = i + 1
        if start != n - 1:
               ss.append((prices[start], prices[n - 1])) 

        m = len(ss)
        merge = [[i for j in xrange(k + 1)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(k):
                pass

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0

        maxsize = (n + 1) / 2 + 1
        sell = [[0 for j in xrange(maxsize)] for i in xrange(n + 1)]
        buy = [[-55555555555555 for j in xrange(maxsize)] for i in xrange(n + 1)]

        for i in xrange(1, n + 1): # at day i
            most_trans = min((i + 1) / 2, k)
            for j in xrange(1, most_trans + 1): # this is j-th transaction
                # print i,j,buy[i][j]
                buy[i][j] = max( buy[i - 1][j], sell[i - 1][j - 1] - prices[i - 1] )

            for j in xrange(1, most_trans + 1): # this is j-th transaction
                # print i,j,sell[i][j]
                sell[i][j] = max( sell[i - 1][j], buy[i - 1][j] + prices[i - 1] )

        # print buy
        # print sell
        return max(sell[n])

sln = Solution()
print sln.maxProfit(2, [2,4,1]) # 2
# print sln.maxProfit(1, [1,2,3]) # 2
# print sln.maxProfit(1, []) # 0
# print sln.maxProfit(1, [0]) # 0
# print sln.maxProfit(1, [5,3,4,2,3,4]) # 2
# print sln.maxProfit(2, [3,2,6,5,0,3]) # 7
# print sln.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]) # 13
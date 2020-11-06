class StockSpanner(object):

    def __init__(self):
        self.lst = []
        self.dp = []
        self.n = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.n += 1
        index = self.n - 1
        self.lst.append(price)
        self.dp.append(-1)
        cur = index - 1
        while cur >= 0 and self.lst[cur] <= price:
            cur = self.dp[cur]
        # cur is the first GT price, or never find
        self.dp[index] = cur
        # print "When input {}, cur = {}".format(price, cur)
        if cur == -1:
            return self.n
        else:
            return index - cur

# # Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# for i in [100, 80, 60, 70, 60, 75, 85]:
# # for i in [31, 41, 48, 59, 79]:
#     print obj.next(i), 
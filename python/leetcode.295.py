from Queue import PriorityQueue
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 维护最大的数，方便放到右边
        self.ql = []
        # 维护最小的数，方便放到左边
        self.qr = []

    def nl(self):
        return len(self.ql)
    def nr(self):
        return len(self.qr)
    # remove left
    def rl(self):
        return -heapq.heappop(self.ql)
    # get left
    def gl(self):
        return -self.ql[0]
    # push left
    def pl(self, x):
        heapq.heappush(self.ql, -x)
    def rr(self):
        return heapq.heappop(self.qr)
    def gr(self):
        return self.qr[0]
    def pr(self, x):
        heapq.heappush(self.qr, x)

    def put_left(self, x):
        if self.nr() == 0:
            self.pl(x)
            return
        if x < self.gr():
            # 如果小于右边的最小值，可以安全加
            self.pl(x)
        else:
            # 需要把右边最小的和左边最大的交换
            if self.nl():
                l = self.rl()
                r = self.rr()
                # print "Switch!! {} to r {} to l".format(l, r)
                self.pl(r)
                self.pl(l)
                self.pr(x)
            else:
                r = self.rr()
                self.pl(r)
                self.pr(x)

    def put_right(self, x):
        if self.nl() == 0:
            self.pr(x)
            return
        if x > self.gl():
            # 如果小于左边的最大值，可以安全加
            self.pr(x)
        else:
            # 需要把右边最小的和左边最大的交换
            if self.nr():
                l = self.rl()
                r = self.rr()
                self.pr(r)
                self.pr(l)
                self.pl(x)
            else:
                l = self.rl()
                self.pr(l)
                self.pl(x)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if self.nl() == self.nr():
            self.put_left(num)
            # print "P EQL {} ql {} qr {}".format(num, self.ql, self.qr)
        elif self.nl() > self.nr():
            # 放到右边
            self.put_right(num)
            # print "P R {}".format(num)
        else:
            self.put_left(num)
            # print "P L {}".format(num)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.nl() == self.nr():
            # print "eq L {} R {}".format(self.gl(), self.gr())
            return (self.gl() + self.gr()) / 2.0
        # print "neq L {} R {}".format(self.gl(), self.gr())
        return self.gl()
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
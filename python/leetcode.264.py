import sys
class Solution(object):
    def __init__(self):
        self.T = []

    def generate(self, n):
        self.T.append(1)
        i = 0
        for i in xrange(1, n):
            last = sys.maxint
            for j in xrange(i):
                chs = filter(lambda x: x > self.T[i - 1], [self.T[j] * 2, self.T[j] * 3, self.T[j] * 5])
                if chs != []:
                    last = min(min(chs), last)
            self.T.append(last)

    def nthUglyNumber1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.T == []:
            self.generate(500)
        return self.T[n - 1]

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = 0
        i3 = 0
        i5 = 0
        ans = [1]
        for i in xrange(1, n):
            x2, x3, x5 = ans[i2], ans[i3], ans[i5]
            t = min([x2 * 2, x3 * 3, x5 * 5])
            if t == x2 * 2:
                i2 += 1
            if t == x3 * 3:
                i3 += 1
            if t == x5 * 5:
                i5 += 1
            ans.append(t)
        return ans[-1]

sln = Solution()
print sln.nthUglyNumber1(355)
print sln.nthUglyNumber(355)
print sln.nthUglyNumber(1)
print sln.nthUglyNumber(20)
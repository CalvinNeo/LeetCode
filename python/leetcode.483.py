import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # find the smallest x where (x ^ k - 1) / (x - 1) == n
        n = int(n)
        for k in xrange(61, 0, -1):
            l = 2
            # print k
            r = n
            def check(x):
                return (x ** k - 1) - (x - 1) * n
            # print "test", k
            # print l, r
            while l < r:
                x = (l + r) / 2
                test = check(x)
                if test < 0:
                    # x too small
                    l = x + 1
                elif test > 0:
                    # x too big
                    r = x - 1
                else:
                    return str(x)
            if check(l) == 0:
                return str(l)
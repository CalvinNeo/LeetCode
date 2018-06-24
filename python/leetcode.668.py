class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        mx = n * m + 1
        l = 1
        r = mx
        def check(mid):
            lc = 0
            me = min(mid, m) + 1
            for step in xrange(1, me):
                ne = min(mid, n * step)
                lc += (ne - step) / step + 1
            return lc

        while l < r:
            mid = (l + r) / 2
            tot = check(mid)
            # print "check {} to be {}".format(mid, tot)
            if tot < k:
                l = mid + 1
            else:
                r = mid
        return l

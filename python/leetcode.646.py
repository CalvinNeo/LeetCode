import bisect
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        inf = 555555555
        dp = [inf for i in xrange(n + 1)]

        # pairs.sort(cmp = lambda x, y:cmp(x[1], y[1]) if x[0] == y[0] else cmp(x[0], y[0]))
        pairs.sort(cmp = lambda x, y:cmp(x[0], y[0]) if x[1] == y[1] else cmp(x[1], y[1]))
        # print pairs
        mlen = 0
        for i in xrange(1, n + 1):
            [s, e] = pairs[i - 1]
            j = bisect.bisect_right(dp, s - 1)
            # print "j", j
            dp[j] = min(e, dp[j])
            mlen = max(mlen, j)
        # print dp
        if dp[mlen] == inf:
            return 0
        else:
            return mlen + 1
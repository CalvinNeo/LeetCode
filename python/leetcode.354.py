class Solution(object):
    def maxEnvelopes1(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0:
            return 0
        dp = [None] * n
        def dfs(cur):
            (w, h) = envelopes[cur]
            if dp[cur] != None:
                return
            else:
                dp[cur] = 1

            for (i, e) in enumerate(envelopes):
                (ww, hh) = e
                if ww < w and hh < h:
                    # print "{} ({}, {}) fits {} ({}, {})".format(cur, w, h, i, ww, hh)
                    if dp[i] == None:
                        dfs(i)
                    dp[cur] = max(dp[cur], dp[i] + 1)
                    # print "dp[i] {} dp[cur] {}".format(dp[i], dp[cur])

        for i in xrange(n):
            dfs(i)

        # print dp
        return max(dp)

    def maxEnvelopes2(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0:
            return 0
        dp = [1] * n
        def cmptp(x, y):
            (w1, h1) = x
            (w2, h2) = y
            if w1 == w2:
                return cmp(h1, h2)
            else:
                return cmp(w1, w2)
        envelopes.sort(cmptp)
        for i in xrange(1, n):
            (w, h) = envelopes[i]
            # Important, must try all possible values
            from bisect import bisect_left
            j = bisect_left(envelopes, envelopes[i])
            while j >= 0:
                (ww, hh) = envelopes[j]
                if ww < w and hh < h:
                    dp[i] = max(dp[j] + 1, dp[i])
                elif ww > w and hh > h:
                    break
                j -= 1
        # Important, not dp[n - 1]
        return max(dp)

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0:
            return 0
        import sys
        dp = [sys.maxint] * n

        def cmptp(x, y):
            (w1, h1) = x
            (w2, h2) = y
            if w1 == w2:
                return cmp(h2, h1)
            else:
                return cmp(w1, w2)

        envelopes.sort(cmptp)
        nums = map(lambda x: x[1], envelopes) 
        from bisect import bisect_left

        for (i, x) in enumerate(nums):
            j = bisect_left(dp, x)
            dp[j] = x

        j = n - 1
        while j >= 0:
            if dp[j] != sys.maxint:
                return j + 1
            j -= 1
        return 0

sln = Solution()
# 0 1 3 3 2
print sln.maxEnvelopes([])
print sln.maxEnvelopes([[5,4]])
print sln.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
print sln.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]])
print sln.maxEnvelopes([[10,8],[1,12],[6,15],[2,18]])

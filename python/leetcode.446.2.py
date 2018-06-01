class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[0 for i in xrange(n + 1)] for j in xrange(n + 1)]
        D = {}
        for (i, x) in enumerate(A):
            if x in D:
                D[x].append(i)
            else:
                D[x] = [i]
        for prev in xrange(0, n):
            for fst in xrange(prev + 1, n):
                # get all snd where A[prev] - A[fst] == A[fst] - A[snd]
                expected = 2 * A[fst] - A[prev]
                if expected in D:
                    for snd in D[expected]:
                        if snd > fst:
                            dp[fst][snd] += (dp[prev][fst] + 1)
        ans = 0
        for fst in xrange(n):
            for snd in xrange(fst + 1, n):
                ans += dp[fst][snd]
        return ans
sln = Solution()
print sln.numberOfArithmeticSlices([2, 4, 6, 8, 10])

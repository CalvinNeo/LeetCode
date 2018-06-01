import bisect
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        M = 10 ** 9 + 7
        n = len(A)
        A.sort()
        dp = [1] * n
        for i in xrange(n):
            x = A[i]
            for lson in xrange(i):
                if x % A[lson] == 0:
                    right = x / A[lson]
                    rson = bisect.bisect_left(A, right)
                    if 0 <= rson < n and A[rson] == right:
                        dp[i] += (dp[lson] * dp[rson]) % M
                        dp[i] %= M
        # print dp
        return sum(dp) % M

sln = Solution()
print sln.numFactoredBinaryTrees([2])
print sln.numFactoredBinaryTrees([2,4])
print sln.numFactoredBinaryTrees([2,4,5,10])
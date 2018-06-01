class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        X0 = sum([ i * A[i] for i in xrange(n)])
        s = sum(A)
        X = X0
        ans = X0
        for i in xrange(1, n):
            X -= (n - 1) * A[(-i % n)]
            X += s - A[(-i % n)]
            ans = max(ans, X)
        return ans
sln = Solution()
print sln.maxRotateFunction([4])
print sln.maxRotateFunction([4, 3, 2, 6])
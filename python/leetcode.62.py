class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def fac(n):
            ans = 1
            for i in xrange(2, n + 1):
                ans *= i
            return ans
        return fac(m + n - 2) / fac(m - 1) / fac(n - 1)
sln = Solution()
print sln.uniquePaths(3,  2)
class Solution(object):
    def fp(self, x, n):
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        r = self.myPow(x, n / 2)
        if n % 2 == 1:
            return r * r * x
        else:
            return r * r
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.fp(x, -n)
        else:
            return self.fp(x, n)
sln = Solution()
print sln.myPow(4, 5)
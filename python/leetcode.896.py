class Solution(object):
    def isMonotonicWA(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 2:
            return True
        for i in xrange(2, n):
            a = (A[i] - A[i - 1])
            b = (A[i - 1] - A[i - 2])
            if a * b < 0:
                return False
            elif a * b == 0 and a + b != 0:
                return False
        return True

    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 2:
            return True
        flag = 0

        def sgn(x):
            return x / abs(x)
        for i in xrange(1, n):
            k = A[i] - A[i - 1]
            if k == 0:
                continue
            news = sgn(k)
            if flag == 0:
                flag = news
            elif flag != news:
                return False

        return True

# sln = Solution()
# print sln.isMonotonic([1,-1,-1,3])
# print sln.isMonotonic([1,2,2,3])

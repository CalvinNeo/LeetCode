class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def bs(l, r):
            while l < r:
                # print l, r
                m = (l + r) / 2
                if m * m == x:
                    return m
                elif m * m < x:
                    if (m + 1) * (m + 1) > x:
                        return m
                    else:
                        l = m + 1
                elif m * m > x:
                    r = m - 1
            return l
        return 0 if x == 0 else bs(1, x)                    

sln = Solution()
print sln.mySqrt(0)
print sln.mySqrt(1)
print sln.mySqrt(2)
print sln.mySqrt(3)
print sln.mySqrt(4)
print sln.mySqrt(9)

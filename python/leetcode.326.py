class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0:
            return False
        return math.log(n, 3).is_integer()


sln = Solution()
print sln.isPowerOfThree(0)
print sln.isPowerOfThree(3)
print sln.isPowerOfThree(4)
print sln.isPowerOfThree(6)
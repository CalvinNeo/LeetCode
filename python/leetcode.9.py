class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        pa = 0
        t = x
        while t > 0:
            m = t % 10
            t /= 10
            pa *= 10
            pa += m
        return True if pa == x else False
sln = Solution()
print sln.isPalindrome(123)
print sln.isPalindrome(0)
print sln.isPalindrome(1)
print sln.isPalindrome(222)
print sln.isPalindrome(123321)
print sln.isPalindrome(12321)
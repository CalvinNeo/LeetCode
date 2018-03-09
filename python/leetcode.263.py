class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        dos = [2,3,5]
        if num == 0:
            return False
        for d in dos:
            while num % d == 0:
                num /= d
        return num == 1

sln = Solution()
print sln.isUgly(0)
print sln.isUgly(1)
print sln.isUgly(2)
print sln.isUgly(6)
print sln.isUgly(7)
print sln.isUgly(8)
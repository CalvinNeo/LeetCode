class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = bin(num)[2:]
        if s.count('0') & 1:
            return False
        s = s.replace('0', '')
        if s == '1':
            return True
        return False

# sln = Solution()
# print sln.isPowerOfFour(16)
# print sln.isPowerOfFour(1)
# print sln.isPowerOfFour(0)
# print sln.isPowerOfFour(5)
# print sln.isPowerOfFour(2)

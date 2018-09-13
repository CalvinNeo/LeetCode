class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        x = num
        a = 0
        while x:
            a += 1
            x /= 2
        mask = (1 << a) - 1
        return (mask & ~num) & 0xffffffff

# sln = Solution()
# print sln.findComplement(1)
# print sln.findComplement(5)
# print sln.findComplement(0)
# print sln.findComplement(2)
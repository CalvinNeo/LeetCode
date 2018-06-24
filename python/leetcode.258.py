class Solution(object):
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num
        else:
            return self.addDigits1(sum([ord(ch) - ord("0") for ch in str(num)]))
    def addDigits(self, num):
        if num == 0:
            return 0
        return (num - 1) % 9 + 1

sln = Solution()
for i in xrange(40):
    print i,
    print sln.addDigits1(i), 
    print sln.addDigits(i)

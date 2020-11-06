class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        if not num:
            return '0'
        s = num / abs(num)
        num = abs(num)
        while num:
            ans += str(num % 7)
            num /= 7
        return ("-" if s < 0 else "") + ''.join(reversed(ans))

# sln = Solution()
# print sln.convertToBase7(100)
# print sln.convertToBase7(-7)
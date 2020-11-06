class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        def check(l):
            if n % l != 0:
                return 0
            flag = 0
            for i in xrange(l, n - l + 1, l):
                flag = 1
                if s[i:i+l] != s[0:l]:
                    return 0
            return flag

        for i in xrange(1, (n + 1) / 2 + 1):
            # print "check", i
            if check(i):
                # print "check true", i
                return True
        return False

# sln = Solution()
# # t f f f f
# print sln.repeatedSubstringPattern('abab')
# print sln.repeatedSubstringPattern('aba')
# print sln.repeatedSubstringPattern('ab')
# print sln.repeatedSubstringPattern('a')
# print sln.repeatedSubstringPattern('')

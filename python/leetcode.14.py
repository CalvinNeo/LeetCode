from bisect import *
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maxlen = 0
        maxlen = reduce(lambda x, y: max(maxlen, len(y)), strs, 0)
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        ans = ""
        for i in xrange(maxlen):
            for j in xrange(len(strs)):
                if len(strs[j]) > i:
                    if strs[j][i] != strs[j - 1][i]:
                        return ans
                else:
                    return ans
            ans += strs[0][i]
        return ans

#class Solution2(object):
#    def longestCommonPrefix(self, strs):
#        """
#        :type strs: List[str]
#        :rtype: str
#        """
#        if len(strs) == 0:
#            return ""
#        elif len(strs) == 1:
#            return strs[0]
#        minlen = 0
#        minlen = reduce(lambda x, y: max(minlen, len(y)), strs, len(strs[0]))
#        l = 0
#        r = minlen - 1
#        while l <= r:
#            mid = (l + r) / 2
#            flag = True
#            for s in strs:
                

sln = Solution()
print sln.longestCommonPrefix(["", ""])
print sln.longestCommonPrefix(["123", "1234", "134"])

#print 0xff & ord('123'[0]) & ord('123'[0])
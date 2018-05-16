class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i in xrange(len(s)):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j < len(t):
                j += 1
            else:
                return False
        return True

sln = Solution()
print sln.isSubsequence("abc", "ahbgdc")
print sln.isSubsequence("axc", "ahbgdc")
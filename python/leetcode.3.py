class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ex = {}
        m = 0
        start = 0
        for i in xrange(len(s)):
            ch = s[i]
            if (not ex.has_key(ch)) or ex[ch] < start:
                ex[ch] = i
            else:
                m = max(m, i - start)
                start = ex[ch] + 1
                ex[ch] = i
        m = max(m, len(s) - start)
        return m
sln = Solution()
print sln.lengthOfLongestSubstring("pwwekp")
print sln.lengthOfLongestSubstring("c")

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        s = s.strip(" ")
        for i in xrange(len(s) - 1, -1, -1):
            if s[i] != " ":
                ans+=1
            else:
                return ans
        return ans
sln = Solution()
print sln.lengthOfLastWord("Hello World")
print sln.lengthOfLastWord("Hello World ")
print sln.lengthOfLastWord("H")
print sln.lengthOfLastWord(" ")
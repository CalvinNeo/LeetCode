class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], filter(lambda x: x, s.split(' '))))[::-1]

sln = Solution()
print sln.reverseWords("the sky is blue")
print sln.reverseWords("2    1")
print sln.reverseWords("    ")
print sln.reverseWords("   a   b ")
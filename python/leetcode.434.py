class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(filter(lambda x: x != "", s.split(" ")))

sln = Solution()
print sln.countSegments("    ")
print sln.countSegments("a   b")
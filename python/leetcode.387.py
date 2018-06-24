class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0] * 256
        for i, x in enumerate(s):
            d[ord(x)] += 1
        for i, x in enumerate(s):
            if d[ord(x)] == 1:
                return i
        return -1
sln = Solution()
print sln.firstUniqChar("abc")
print sln.firstUniqChar("aab")
print sln.firstUniqChar("")
print sln.firstUniqChar("aa")
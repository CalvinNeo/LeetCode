class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <= 10:
            return []
        ans = []
        d = dict()
        for i in xrange(n - 10 + 1):
            if s[i:i+10] in d:
                d[s[i:i+10]] += 1
            else:
                d[s[i:i+10]] = 1
        for (k, v) in d.iteritems():
            if v >= 2:
                ans.append(k)
        return ans

sln = Solution()
print sln.findRepeatedDnaSequences("AAAAAAAAAAA")
print sln.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
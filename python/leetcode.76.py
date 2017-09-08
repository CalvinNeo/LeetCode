class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cd = {}
        d = {}
        length = len(s)
        for c in t:
            if cd.has_key(c):
                cd[c] += 1
            else:
                cd[c] = 1
            d[c] = length
        l = 0
        import sys
        res = sys.maxint
        resstr = ""
        for i in xrange(length):
            c = s[i]
            if c in d.keys():
                d[c] = i
            lst = [(k, d[k]) for k in sorted(d, key=d.get)]
            # print lst
            if lst[-1][1] - lst[0][1] + 1 < res:
                resstr = s[lst[0][1]:lst[-1][1]+1]
                res = lst[-1][1] - lst[0][1] + 1
        return resstr

sln = Solution()
print sln.minWindow("ADOBECODEBANC", "ABC")
print sln.minWindow("A", "B")
print sln.minWindow("B", "B")
print sln.minWindow("AAA", "A")
            

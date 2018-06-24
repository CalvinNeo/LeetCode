class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in s:
            if not c in d:
                d[c] = 0
            d[c] += 1
        ans = ""
        arr = sorted(d.iteritems(), key = lambda item: item[1], reverse = True)
        for (i, f) in arr:
            if f == 0:
                break
            ans += (i * f)
        return ans
sln = Solution()
print sln.frequencySort("tree")
print sln.frequencySort("cccaaa")
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        mx = max(citations)
        bk = [0] * (mx + 1)
        for i, x in enumerate(citations):
            bk[x] += 1
        tot = 0
        for i in xrange(mx, -1, -1):
            tot += bk[i]
            if tot >= i:
                return min(tot, i)
        return 0

sln = Solution()
print sln.hIndex([1,3,0,5,6]) # 3
print sln.hIndex([1]) # 1
print sln.hIndex([]) # 0
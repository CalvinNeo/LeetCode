class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in xrange(1 << n):
            ans.append(i ^ (i >> 1))
        return ans

sln = Solution()
print sln.grayCode(2)
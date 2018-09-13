class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[0 for i in xrange(n + 1)] for n in xrange(numRows)]
        ans[0][0] = 1
        for i in xrange(1, numRows):
            for j in xrange(i + 1):
                if 0 <= j <= i - 1:
                    ans[i][j] += ans[i - 1][j]
                if 0 <= j - 1 <= i - 1:
                    ans[i][j] += ans[i - 1][j - 1]
        return ans

# sln = Solution()
# print sln.generate(5)
# print sln.generate(1)
# print sln.generate(0)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        elif n == 1:
            return triangle[0][0]

        inf = 555555555
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        dp[0][0] = triangle[0][0]
        for i in xrange(1, n):
            for j in xrange(0, i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[n - 1])

sln = Solution()
print sln.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
print sln.minimumTotal([[1],[-2,-5],[3,6,9],[-1,2,4,-3]])

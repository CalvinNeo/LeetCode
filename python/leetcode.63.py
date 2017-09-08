class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        m = len(obstacleGrid) 
        n = len(obstacleGrid[0])
        ans = [[0 for j in xrange(n)] for i in xrange(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            ans[0][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = 0
                    if i > 0:
                        ans[i][j] += ans[i - 1][j]
                    if j > 0:
                        ans[i][j] += ans[i][j - 1]
        print ans
        return ans[m-1][n-1]

sln = Solution()
print sln.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
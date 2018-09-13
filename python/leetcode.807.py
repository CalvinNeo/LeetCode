class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        clim = [0 for i in xrange(m)]
        rlim = [0 for i in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                clim[j] = max(clim[j], grid[i][j])
                rlim[i] = max(rlim[i], grid[i][j])
        s = 0

        for i in xrange(n):
            for j in xrange(m):
                dc = clim[j] - grid[i][j]
                dr = rlim[i] - grid[i][j]
                s += min(dc, dr)
        return s

sln = Solution()
print sln.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
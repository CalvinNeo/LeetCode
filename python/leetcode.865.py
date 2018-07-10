# 865 c92.4

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
        	return 0
        m = len(grid[0])

        vis = [[0 for i in xrange(m)] for j in xrange(n)]
        K = [0] * 6
        def dfs(x, y):

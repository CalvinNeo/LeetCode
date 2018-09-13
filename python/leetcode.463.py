class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        vis = [[0 for i in xrange(m)] for j in xrange(n)]

        tot_cell = 0
        inner_edge = 0

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j]:
                    tot_cell += 1

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        DX = [-1, 0, 0, 1]
        DY = [0, -1, 1, 0]
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j]:
                    for (dx, dy) in zip(DX, DY):
                        nx = i + dx
                        ny = j + dy
                        if valid(nx, ny) and grid[nx][ny] == 1:
                            inner_edge += 1

        return 4 * tot_cell - inner_edge

# sln = Solution()
# print sln.islandPerimeter([[0,1,0,0],
#      [1,1,1,0],
#      [0,1,0,0],
#      [1,1,0,0]]) # 16
# print sln.islandPerimeter([[1,1], [1,1]]) # 8
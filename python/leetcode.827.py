class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        conn = 1
        self.cnt = 0
        vis = [[0 for i in xrange(n)] for j in xrange(n)]
        conn_size = [0 for i in xrange(n * n + 10)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        def dfs(sx, sy, dom):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            if grid[sx][sy] == 0:
                return
            grid[sx][sy] = dom
            vis[sx][sy] = 1
            self.cnt += 1
            for (dx, dy) in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y] and grid[x][y] != 0:
                    dfs(x, y, dom)

        for i in xrange(n):
            for j in xrange(n):
                if not vis[i][j] and grid[i][j] == 1:
                    self.cnt = 0
                    dfs(i, j, conn)
                    conn_size[conn] = self.cnt
                    conn += 1

        ans = max(conn_size)
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == 0:
                    DX = [-1, 0, 0, 1]
                    DY = [0, -1, 1, 0]
                    xs = [i + dx for dx in DX]
                    ys = [j + dy for dy in DY]
                    newans = 1
                    for (c1, (x, y)) in enumerate(zip(xs, ys)):
                        if valid(x, y):
                            flag = 0
                            for c2 in xrange(c1):
                                if valid(xs[c2], ys[c2]) and grid[xs[c2]][ys[c2]] == grid[x][y]:
                                    flag = 1
                                    break
                            if flag:
                                pass
                            else:
                                newans += conn_size[grid[x][y]]
                            # print "({} {}) = {}".format(x, y, conn_size[grid[x][y]])
                        ans = max(ans, newans)
        # print conn_size
        return ans
sln = Solution()
print sln.largestIsland([[1,0,0,1,1],[1,0,0,1,0],[1,1,1,1,1],[1,1,1,0,1],[0,0,0,1,0]])
print sln.largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]])
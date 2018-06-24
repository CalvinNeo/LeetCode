# coding: utf8
class Solution(object):
    def swimInWaterWA(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0

        inf = 5555555555
        # 这个错误在于路径是可以交叉的，并且还和之前的路径有关，所以不能缓存
        vis = [[0 for i in xrange(n)] for j in xrange(n)]
        dp = [[[-1 for i in xrange(n)] for j in xrange(n)] for k in xrange(4)]
        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        def dfs(sx, sy):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            if sx == n - 1 and sy == n - 1:
                return grid[sx][sy]
            best_choice = inf
            for (i, (dx, dy)) in enumerate(zip(DX, DY)):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y]:
                    if dp[i][sx][sy] != -1:
                        goto_i = dp[i][sx][sy]
                    else:
                        vis[sx][sy] = 1
                        goto_i = max(dfs(x, y), grid[sx][sy])
                        vis[sx][sy] = 0
                        dp[i][sx][sy] = goto_i
                    best_choice = min(goto_i, best_choice)
            return best_choice

        return dfs(0, 0)

    def swimInWaterTLE(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0

        inf = 5555555555
        self.mind = inf
        vis = [[0 for i in xrange(n)] for j in xrange(n)]
        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        def dfs(sx, sy, v):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            if sx == n - 1 and sy == n - 1:
                self.mind = min(self.mind, v)
            for (dx, dy) in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y] and v < self.mind:
                    vis[sx][sy] = 1
                    dfs(x, y, max(v, grid[x][y]))
                    vis[sx][sy] = 0
        dfs(0, 0, grid[0][0])
        return self.mind

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0

        inf = 5555555555
        self.mind = inf
        vis = [[0 for i in xrange(n)] for j in xrange(n)]
        dp = [[inf for i in xrange(n)] for j in xrange(n)]
        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        def dfs(sx, sy, v):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            if sx == n - 1 and sy == n - 1:
                self.mind = min(self.mind, v)
                return self.mind
            if v > dp[sx][sy]:
                return inf
            best_choice = inf
            for (dx, dy) in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y] and v < self.mind:
                    vis[sx][sy] = 1
                    goto_i = dfs(x, y, max(v, grid[x][y]))
                    best_choice = min(best_choice, goto_i)
                    vis[sx][sy] = 0
            dp[sx][sy] = min(dp[sx][sy], best_choice)
            return best_choice
        dfs(0, 0, grid[0][0])
        return self.mind

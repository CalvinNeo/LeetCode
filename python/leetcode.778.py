# coding: utf8
import Queue
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
        # 这个错误在于路径是可以交叉的(不过这个应该没关系)，并且还和之前的路径有关，所以不能缓存
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

    def swimInWaterACBinarySearch(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        inf = 5555555555

        def test(level):
            vis = [[0 for i in xrange(n)] for j in xrange(n)]
            def valid(x, y):
                return 0 <= x < n and 0 <= y < n
            def dfs(sx, sy):
                DX = [-1, 0, 0, 1]
                DY = [0, -1, 1, 0]
                vis[sx][sy] = 1
                if sx == n - 1 and sy == n - 1:
                    return True
                for (dx, dy) in zip(DX, DY):
                    x = sx + dx
                    y = sy + dy
                    if valid(x, y) and not vis[x][y] and level >= grid[x][y]:
                        if dfs(x, y):
                            return True
                return False
            return dfs(0, 0)

        mx = -inf
        for i in xrange(n):
            for j in xrange(n):
                mx = max(mx, grid[i][j])
        l = grid[0][0]
        r = mx
        while l < r:
            mid = (l + r) / 2
            if test(mid):
                # print "OK", mid
                r = mid
            else:
                # print "Fail", mid
                l = mid + 1
        return l

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        inf = 5555555555
        q = Queue.PriorityQueue()
        class Cell(object):
            def __init__(self, x, y, mx):
                self.x = x
                self.y = y
                self.mx = mx
            def __cmp__(self, other):
                return cmp(grid[self.x][self.y], grid[other.x][other.y])

        vis = [[0 for i in xrange(n)] for j in xrange(n)]
        q.put(Cell(0, 0, grid[0][0]))
        vis[0][0] = 1
        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        while q.qsize() > 0:
            cell = q.get()
            sx, sy = cell.x, cell.y
            if sx == n - 1 and sy == n - 1:
                return cell.mx
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            for (dx, dy) in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y]:
                    vis[x][y] = 1
                    q.put(Cell(x, y, max(cell.mx, grid[x][y])))
# sln = Solution()
# print sln.swimInWater([[0,2],[1,3]]) # 3
# print sln.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) # 16
# print sln.swimInWater([[26,99,80,1,89,86,54,90,47,87],[9,59,61,49,14,55,77,3,83,79],[42,22,15,5,95,38,74,12,92,71],[58,40,64,62,24,85,30,6,96,52],[10,70,57,19,44,27,98,16,25,65],[13,0,76,32,29,45,28,69,53,41],[18,8,21,67,46,36,56,50,51,72],[39,78,48,63,68,91,34,4,11,31],[97,23,60,17,66,37,43,33,84,35],[75,88,82,20,7,73,2,94,93,81]]) # 
# print sln.swimInWater([[67,27,74,98,75,23,15,25,22,29],[51,3,76,62,0,16,94,57,96,55],[72,5,50,39,87,31,1,45,38,36],[88,80,21,99,93,70,10,71,61,77],[97,13,79,73,47,24,8,63,30,26],[11,90,48,19,92,17,35,14,34,28],[53,49,6,4,52,64,65,2,44,83],[46,89,58,20,60,78,7,91,33,69],[37,68,40,82,43,56,81,84,66,59],[32,86,9,95,41,85,12,42,54,18]]) # 67

def wrapWith(mat, x):
    n = len(mat)
    if n == 0:
        return []
    m = len(mat[0])
    return [[x] * (m + 2)] + map(lambda line: [x] + line + [x], mat) + [[x] * (m + 2)]

import Queue
class Cell(object):
    def __init__(self, mat, x, y):
        self.x = x
        self.y = y
        self.mat = mat

    def __cmp__(self, other):
        return cmp(self.mat[self.x][self.y], other.mat[other.x][other.y])

class Solution(object):
    def trapRainWater1(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        inf = 5555555555555
        n = len(heightMap)
        if n == 0:
            return 0
        m = len(heightMap[0])
        ans = 0
        pq = Queue.Queue()
        level = [[inf for i in xrange(m)] for j in xrange(n)]

        for x in xrange(0, n):
            for y in xrange(0, m):
                if x in [0, n - 1] or y in [0, m - 1]:
                    level[x][y] = heightMap[x][y]
                    pq.put((x, y))

        adx = [-1, 0, 0, 1]
        ady = [0, -1, 1, 0]

        def valid(x, y):
            return x >= 0 and x < n and y >= 0 and y < m

        def in_border(x, y):
            return x >= 1 and x < n - 1 and y >= 1 and y < m - 1

        while pq.qsize() > 0:
            x, y = pq.get()
            for (dx, dy) in zip(adx, ady):
                nx, ny = x + dx, y + dy
                if in_border(nx, ny):
                    limit = max(heightMap[nx][ny], level[x][y])
                    if level[nx][ny] > limit:
                        level[nx][ny] = limit
                        pq.put((nx, ny))

        for x in xrange(0, n):
            for y in xrange(0, m):
                if level[x][y] > heightMap[x][y]:
                    ans += level[x][y] - heightMap[x][y]
        return ans


    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        inf = 5555555555555
        n = len(heightMap)
        if n == 0:
            return 0
        m = len(heightMap[0])
        ans = 0
        pq = Queue.PriorityQueue()
        level = [[0 for i in xrange(m)] for j in xrange(n)]

        adx = [-1, 0, 0, 1]
        ady = [0, -1, 1, 0]

        def valid(x, y):
            return x >= 0 and x < n and y >= 0 and y < m

        for x in xrange(0, n):
            for y in xrange(0, m):
                level[x][y] = heightMap[x][y]

        for x in xrange(0, n):
            for y in xrange(0, m):
                if x in [0, n - 1] or y in [0, m - 1]:
                    pass
                else:
                    pq.put(Cell(level, x, y))

        vis = [[0 for i in xrange(m)] for j in xrange(n)]
        def dfs(x, y, h):
            barrier = inf
            vis[x][y] = 1
            for (dx, dy) in zip(adx, ady):
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    if not vis[nx][ny]:
                        if level[nx][ny] < h:
                            return 0
                        elif level[nx][ny] == h:
                            barrier = min(barrier, dfs(nx, ny, h))
                        else:
                            barrier = min(barrier, level[nx][ny])
                else:
                    return 0
            return barrier

        while pq.qsize() > 0:
            cell = pq.get()
            x, y = cell.x, cell.y
            h = level[x][y]
            barrier = inf
            # print "handle ({}, {}), ori level = {}".format(x, y, level[x][y])
            for (dx, dy) in zip(adx, ady):
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    if level[nx][ny] == level[x][y]:
                        vis = [[0 for i in xrange(m)] for j in xrange(n)]
                        vis[x][y] = 1
                        barrier = min(barrier, dfs(nx, ny, h))
                    else:
                        barrier = min(barrier, level[nx][ny])
            if barrier > h:
                # then (x, y) can contain
                level[x][y] = barrier
                pq.put(Cell(level, x, y))

        # print level
        for x in xrange(0, n):
            for y in xrange(0, m):
                if level[x][y] > heightMap[x][y]:
                    ans += level[x][y] - heightMap[x][y]
        return ans

sln = Solution()
print sln.trapRainWater([[1,1,1],[1,0,1],[1,1,1]]) # 1
print sln.trapRainWater([[1,3,2],[3,2,4],[2,3,1]]) # 1
print sln.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) # 4
print sln.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]) # 14

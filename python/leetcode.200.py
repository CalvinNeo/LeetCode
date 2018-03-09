class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0

        N = n * m
        fa = range(N)

        def find(v):
            if fa[v] == v:
                return v
            else:
                return find(fa[v])

        def merge(a, b):
            aa = find(a)
            bb = find(b)
            if aa != bb:
                fa[aa] = bb

        def gi(i, j):
            return i * m + j

        def gc(i):
            return (i / m, i % m)

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == '1': # don't miss that!
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        merge(gi(i - 1, j), gi(i, j))
                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        merge(gi(i, j - 1), gi(i, j))
                    if i + 1 < n and grid[i + 1][j] == '1':
                        merge(gi(i + 1, j), gi(i, j))
                    if j + 1 < m and grid[i][j + 1] == '1':
                        merge(gi(i, j + 1), gi(i, j))
        s = set()
        for i in xrange(N):
            (x, y) = gc(i)
            if grid[x][y] == '1':
                # print "hit", i, find(i)
                s |= set([find(i)])
        return len(s)

sln = Solution()
# 1 3 1 0 4 1

print sln.numIslands(["11110","11010","11000","00000"])
print sln.numIslands(["11000","11000","00100","00011"])
print sln.numIslands(["1"])
print sln.numIslands(["0"])
print sln.numIslands(["010","101","010"])
print sln.numIslands(["10111","10101","11101"])
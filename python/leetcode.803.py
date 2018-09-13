class Solution(object):
    def hitBricksTLE(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        if n == 0:
            return []
        m = len(grid[0])

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        tot = 0
        for x in xrange(n):
            for y in xrange(m):
                tot += grid[x][y]

        vis = [[0 for i in xrange(m)] for j in xrange(n)]
        def dfs(sx, sy):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            vis[sx][sy] = 1
            for dx, dy in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y] and grid[x][y]:
                    dfs(x, y)

        ans = []
        for [hx, hy] in hits:
            grid[hx][hy] = 0
            d = 0
            vis = [[0 for i in xrange(m)] for j in xrange(n)]
            for y in xrange(m):
                if grid[0][y]:
                    dfs(0, y)
            for x in xrange(n):
                for y in xrange(m):
                    if grid[x][y] and not vis[x][y]:
                        d += 1
                        grid[x][y] = 0
            ans.append(d)
            # tot = d
        return ans

    def hitBricksWA(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        if n == 0:
            return []
        m = len(grid[0])

        old_grid = [[x for x in l] for l in grid]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        for [hx, hy] in hits:
            grid[hx][hy] = 0

        def index(x, y):
            return x * m + y + 1
        def loc(i):
            return (i - 1) / m, (i - 1) % m

        vis = [[0 for i in xrange(m)] for j in xrange(n)]
        fa = range(n * m + 1)
        conn_cnt = [1] * (n * m + 1)
        def get_fa(x):
            while fa[x] != x:
                x = fa[x]
            return x

        def dfs(sx, sy, connid):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            domx, domy = loc(connid)
            if not vis[sx][sy] and not (sx == domx and sy == domy):
                conn_cnt[connid] += 1
            if not (sx == domx and sy == domy):
                conn_cnt[index(sx, sy)] = 0
            fa[index(sx, sy)] = connid
            vis[sx][sy] = connid
            for dx, dy in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y] and grid[x][y]:
                    dfs(x, y, connid)

        for x in xrange(n):
            for y in xrange(m):
                if grid[x][y] and not vis[x][y]:
                    connid = index(x, y)
                    dfs(x, y, connid)

        hard_core_index = []
        for y in xrange(m):
            if vis[0][y]:
                hard_core_index.append(vis[0][y])
        hard_core_index = set(hard_core_index)

        def move_to(p, q):
            # set p's father to q
            # print "set {}'s father to {}".format(p, q)
            fa[p] = q
            aaa = conn_cnt[p]
            conn_cnt[q] += conn_cnt[p]
            conn_cnt[p] = 0
            return aaa

        def merge(p, q):
            pfa = get_fa(p)
            qfa = get_fa(q)
            aaa = 0
            # print "pfa {} cnt {}, qfa {} cnt {}".format(pfa, conn_cnt[pfa], qfa, conn_cnt[qfa]), hard_core_index
            if pfa == qfa:
                aaa = 0
            elif (qfa in hard_core_index and pfa in hard_core_index) or (qfa not in hard_core_index and pfa not in hard_core_index):
                move_to(pfa, qfa)
            elif qfa in hard_core_index:
                # attach (x, y) to (hx, hy)
                aaa = move_to(pfa, qfa)
            elif pfa in hard_core_index:
                # attach (hx, hy) to (x, y)
                aaa = move_to(qfa, pfa)
            # print "final {} {}, aaa {}".format(conn_cnt[pfa], conn_cnt[qfa], aaa)
            return aaa
        # print fa
        # print vis
        # print hard_core_index
        # print conn_cnt
        # print old_grid
        # print grid
        ans = []
        hn = len(hits)
        for i in xrange(hn - 1, -1, -1):
            [hx, hy] = hits[i]
            if old_grid[hx][hy] == 0:
                # print "SKIP", i, hx, hy
                ans.append(0)
                continue
            elif grid[hx][hy] == 1:
                ans.append(0)
                continue
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            d = 0
            grid[hx][hy] = 1
            if not vis[hx][hy] and hx == 0:
                connid = index(hx, hy)
                dfs(hx, hy, connid)
                hard_core_index |= set([vis[hx][hy]])
            # print "HANDLE", hx , hy
            prev = get_fa(index(hx, hy))
            for pdx, pdy in zip(DX, DY):
                px, py = hx + pdx, hy + pdy
                if valid(px, py) and grid[px][py]:
                    p, h = index(px, py), index(hx, hy)
                    # print "merge {}[{}] and {}[{}] ".format(p, get_fa(p), h, get_fa(h))
                    # print "cnt", conn_cnt
                    delta = merge(p, h)
                    d += delta
                    # print "delta", delta, "fa", fa
                    # print "========="
            if prev not in hard_core_index and get_fa(index(hx, hy)) in hard_core_index:
                d -= 1
            ans.append(max(d, 0))
        return ans[::-1]

    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        if n == 0:
            return []
        m = len(grid[0])

        old_grid = [[x for x in l] for l in grid]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        for [hx, hy] in hits:
            grid[hx][hy] = 0

        def index(x, y):
            return x * m + y + 1
        def loc(i):
            return (i - 1) / m, (i - 1) % m

        vis = [[0 for i in xrange(m)] for j in xrange(n)]
        fa = range(n * m + 1)
        conn_cnt = [1] * (n * m + 1)
        def get_fa(x):
            while fa[x] != x:
                x = fa[x]
            return x

        def dfs(sx, sy, connid):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            domx, domy = loc(connid)
            if not vis[sx][sy] and not (sx == domx and sy == domy):
                conn_cnt[connid] += 1
            if not (sx == domx and sy == domy):
                conn_cnt[index(sx, sy)] = 0
            fa[index(sx, sy)] = connid
            vis[sx][sy] = connid
            for dx, dy in zip(DX, DY):
                x = sx + dx
                y = sy + dy
                if valid(x, y) and not vis[x][y] and grid[x][y]:
                    dfs(x, y, connid)

        for x in xrange(n):
            for y in xrange(m):
                if grid[x][y] and not vis[x][y]:
                    connid = index(x, y)
                    dfs(x, y, connid)

        hard_core_index = []
        for y in xrange(m):
            if vis[0][y]:
                hard_core_index.append(vis[0][y])
        hard_core_index = set(hard_core_index)

        def move_to(p, q):
            # set p's father to q
            # print "set {}'s father to {}".format(p, q)
            fa[p] = q
            aaa = conn_cnt[p]
            conn_cnt[q] += conn_cnt[p]
            conn_cnt[p] = 0
            return aaa

        def merge(p, h):
            pfa = get_fa(p)
            hfa = get_fa(h)
            aaa = 0
            # print "pfa {} cnt {}, hfa {} cnt {}".format(pfa, conn_cnt[pfa], hfa, conn_cnt[hfa]), hard_core_index
            if pfa == hfa:
                aaa = 0
            elif (hfa in hard_core_index and pfa in hard_core_index) or (hfa not in hard_core_index and pfa not in hard_core_index):
                move_to(pfa, hfa)
            elif hfa in hard_core_index:
                # attach (x, y) to (hx, hy)
                aaa = move_to(pfa, hfa)
            elif pfa in hard_core_index:
                # attach (hx, hy) to (x, y)
                # should not include (hx, hy)
                aaa = move_to(hfa, pfa) - 1
            # print "final {} {}, aaa {}".format(conn_cnt[pfa], conn_cnt[hfa], aaa)
            return aaa
        # print fa
        # print vis
        # print hard_core_index
        # print conn_cnt
        # print old_grid
        # for g in grid:
        #     print g
        ans = []
        hn = len(hits)
        for i in xrange(hn - 1, -1, -1):
            [hx, hy] = hits[i]
            if old_grid[hx][hy] == 0:
                # print "SKIP", i, hx, hy
                ans.append(0)
                continue
            elif grid[hx][hy] == 1:
                ans.append(0)
                continue
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            d = 0
            grid[hx][hy] = 1
            if not vis[hx][hy] and hx == 0:
                # connid = index(hx, hy)
                # dfs(hx, hy, connid)
                # hard_core_index |= set([vis[hx][hy]])
                connid = index(hx, hy)
                for pdx, pdy in zip(DX, DY):
                    px, py = hx + pdx, hy + pdy
                    if valid(px, py) and grid[px][py] and get_fa(index(px, py)) in hard_core_index:
                        merge(index(hx, hy), index(px, py))
                if get_fa(index(hx, hy)) == connid:
                    hard_core_index |= set([connid])
            # print "HANDLE", hx , hy
            prev = get_fa(index(hx, hy))
            for pdx, pdy in zip(DX, DY):
                px, py = hx + pdx, hy + pdy
                if valid(px, py) and grid[px][py]:
                    p, h = index(px, py), index(hx, hy)
                    # print "merge {}[{}] and {}[{}] ".format(p, get_fa(p), h, get_fa(h))
                    # print "cnt", conn_cnt
                    delta = merge(p, h)
                    d += delta
                    # print "delta", delta, "fa", fa
                    # print "========="
            ans.append(max(d, 0))
        ans = ans[::-1]
        # for i, [x, y] in zip(ans, hits):
        #     print "{} [{} {}]".format(i, x, y)
        return ans


# sln = Solution()
# print sln.hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]]) # [2]
# print sln.hitBricks([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]]) # [0, 0]
# print sln.hitBricks([[1,0],[1,1]], [[1,1],[1,0]]) # [0, 0]
# print sln.hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]]) # [1,0,1,0,0]
# print sln.hitBricks([[1,0,1],[1,1,1]], [[0,0],[0,2],[1,1]]) # [0,3,0]
# print sln.hitBricks([[1,1,1],[0,1,0],[0,0,0]], [[0,2],[2,0],[0,1],[1,2]]) # [[0,0,1,0]]
# print sln.hitBricks([[1,1,1,0,1,1,1,1],[1,0,0,0,0,1,1,1],[1,1,1,0,0,0,1,1],[1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]], [[4,6],[3,0],[2,3],[2,6],[4,1],[5,2],[2,1]]) # [0,2,0,0,0,0,2]

# print sln.hitBricks([[0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[0,0,0,1,0,0,1,1,1],[0,0,1,1,0,1,1,1,0],[0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,0]], 
#     [[1,8],[2,1],[1,4],[3,0],[3,4],[0,7],[1,6],[0,8],[2,5],[3,2],[2,0],[0,2],[0,5],[0,1],[4,8],[3,7],[0,6],[5,7],[5,3],
#     [2,6],[2,2],[5,8],[2,8],[4,0],[3,3],[1,1],[0,0],[4,7],[0,3],[2,4],[3,1],[1,0],[5,2],[3,8],[4,2],[5,0],[1,2],[1,7],
#     [3,6],[4,1],[5,6],[0,4],[5,5],[5,4],[1,5],[4,4],[3,5],[4,6],[2,3],[2,7]]) # [0,0,0,0,0,0,12,0] 

# print sln.hitBricks([[0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[0,0,0,1,0,0,1,1,1],[0,0,1,1,0,1,1,1,0],[0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,0]], 
#     [[1,4],[1,6],[0,2],[0,5],[1,5]]) # [0, 0, 0, 1, 0]
# print sln.hitBricksTLE([[1,1,1],[1,1,1]], [[1,0],[1,2],[0,1],[1,1]])

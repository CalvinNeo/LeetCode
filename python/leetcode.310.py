class Solution(object):
    def findMinHeightTreesTLE(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        inf = 555555555555555
        dis = [[inf for i in xrange(n)] for j in xrange(n)]

        for i in xrange(n):
            dis[i][i] = 0

        for [a, b] in edges:
            dis[a][b] = 1
            dis[b][a] = 1

        for i in xrange(n):
            for j in xrange(n):
                for k in xrange(n):
                    if dis[i][k] + dis[k][j] < dis[i][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]

        mx = [0 for i in xrange(n)]
        for i in xrange(n):
            mx[i] = max(dis[i])

        mmi = min(mx)
        ans = []
        for i in xrange(n):
            if mx[i] == mmi:
                ans.append(i)
        return ans

    def findMinHeightTreesTLE2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        inf = 555555555555555

        import Queue

        conn = [[] for i in xrange(n)]
        for [a, b] in edges:
            conn[a].append(b)
            conn[b].append(a)

        def bfs(start):
            vis = [0] * n
            q = Queue.Queue()
            q.put((start, 0))
            mx = 0
            while not q.empty():
                cur, d = q.get()
                mx = max(d, mx)
                vis[cur] = 1
                for nxt in conn[cur]:
                    if not vis[nxt]:
                        q.put((nxt, d + 1))
            return mx

        mx = [bfs(i) for i in xrange(n)]

        mmi = min(mx)
        ans = []
        for i in xrange(n):
            if mx[i] == mmi:
                ans.append(i)
        return ans

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        inf = 555555555555555

        if n <= 2:
            return range(n)

        import Queue

        conn = [[] for i in xrange(n)]
        ind = [0 for i in xrange(n)]
        for [a, b] in edges:
            conn[a].append(b)
            conn[b].append(a)
            ind[a] += 1
            ind[b] += 1

        ans = []
        q = Queue.Queue()
        def del_leaf():
            for i in xrange(n):
                if ind[i] == 1:
                    q.put(i)
                    ind[i] -= 1
                    # print "del leaf {}".format(i)

        comp = 0
        while comp < n - 2:
            del_leaf()
            while not q.empty():
                l = q.get()
                comp += 1
                if comp == n:
                    ans = [l]
                    break
                for nxt in conn[l]:
                    ind[nxt] -= 1
                    # print "ind[{}] = {}".format(nxt, ind[nxt])
                    if ind[nxt] == 0:
                        # print "remove {}".format(nxt)
                        q.put(nxt)

        if comp < n:
            for i in xrange(n):
                if ind[i] > 0:
                    ans.append(i)
        return ans

# sln = Solution()
# print sln.findMinHeightTrees(2, [[0, 1]]) # [0, 1]
# print sln.findMinHeightTrees(1, []) # [0]
# print sln.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) # [1]
# print sln.findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) # [3, 4]
# print sln.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]) # [3]

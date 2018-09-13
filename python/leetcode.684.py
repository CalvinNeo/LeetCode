class Solution(object):
    def findRedundantConnectionWA(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        vis = [0 for i in xrange(n + 1)]

        conn = [[] for i in xrange(n + 1)]

        for [f, t] in edges:
            conn[f].append(t)
            conn[t].append(f)

        self.to_remove = None

        def dfs(cur, fr):
            vis[cur] = 1
            for nxt in conn[cur]:
                if vis[nxt] == 1 and nxt != fr:
                    ne = sorted([cur, nxt])
                    if not self.to_remove:
                        self.to_remove = ne
                        print "A", self.to_remove
                    elif edges.index(ne) > edges.index(self.to_remove):
                        self.to_remove = ne
                        print "B", self.to_remove
                elif vis[nxt] == 0:
                    dfs(nxt, cur)

            vis[cur] = 2

        dfs(1, -1)
        return self.to_remove

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)

        fa = [i for i in xrange(n + 1)]

        def gfa(x):
            while x != fa[x]:
                x = fa[x]
            return x

        def mer(x, y):
            fx = gfa(x)
            fy = gfa(y)
            fa[fx] = fy

        for [f, t] in edges:
            fx = gfa(f)
            fy = gfa(t)
            if fx == fy:
                return sorted([f, t])
            else:
                mer(f, t)


sln = Solution()
print sln.findRedundantConnection([[1,2], [1,3], [2,3]]) # 2, 3
print sln.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]) # 1, 4

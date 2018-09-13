class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        conn = [[] for i in xrange(N)]
        dist = [[-1 for i in xrange(N)] for j in xrange(N)]

        for [f, t] in edges:
            conn[f].append(t)
            conn[t].append(f)

        def dfs1(cur):
            for nxt in conn[cur]:
                dist[nxt][cur] = 1
                dist[cur][nxt] = 1
                dfs(nxt)

        def dfs(cur, node, deep):
            dist[cur][node] = deep
            dist[node][cur] = deep
            for nxt in conn[cur]:
                dfs(nxt, node, deep)

        def update(cur):
            ll = len(conn[cur])
            for n1 in xrange(ll):
                for n2 in xrange(n1 + 1, ll):
                    
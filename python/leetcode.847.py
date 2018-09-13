def set_bit(x, i):
    return x | (1 << i)

def get_bit(x, i):
    return x & (1 << i)

def print_bit(X):
    i = 0
    ans = []
    while X:
        if X & 1:
            ans.append(i)
        i += 1
        X /= 2
    return ';'.join(map(str, ans))

class Solution(object):
    def shortestPathLengthWA(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        inf = 555555555
        n = len(graph)
        dist = [[inf for i in xrange(n)] for j in xrange(n)]
        for i, e in enumerate(graph):
            dist[i][i] = 0
            for j in e:
                dist[i][j] = dist[j][i] = 1

        for z in xrange(n):
            for x in xrange(n):
                for y in xrange(n):
                    dist[x][y] = min(dist[x][y], dist[x][z] + dist[z][y])

        dp = [[None for j in xrange(n + 1)] for i in xrange(2 ** 12 + 10)]

        # for d in dist:
        #     print d

        def clsAll():
            for i in xrange(2 ** 12 + 10):
                for j in xrange(n + 1):
                    dp[i][j] = None

        def dfs(s, v, prev, tot, fr):
            # Important: This is not OK
            # if tot == n:
            #     return prev

            if s == (1 << (n)) - 1:
                return prev

            if dp[s][v] != None:
                return dp[s][v]

            d = inf
            a = set_bit(s, v)
            # print "cur {} s {} prev {} fr {}".format(v, print_bit(s), prev, fr)
            for nv in xrange(n):
                if not get_bit(s, nv):
                    ns = set_bit(s, nv)
                    # print "dist[{}][{}]={}".format(v, nv, dist[v][nv])
                    dd = dfs(ns, nv, prev + dist[v][nv], tot + 1, v)
                    d = min(d, dd)
                    # print "cur {} next {} d {}".format(v, nv, dd)

            # print "({}, {})".format(prev, d)
            # print "to {} least dist {}".format(v, d)
            dp[s][v] = d
            return dp[s][v]
        
        # clsAll()
        # dfs(set_bit(0, 5), 5, 0, 1, None)

        mi = inf
        for i in xrange(n):
            clsAll()
            c = dfs(set_bit(0, i), i, 0, 1, None)
            # print i, c
            mi = min(mi, c)
        return mi


    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        inf = 555555555
        n = len(graph)
        dist = [[inf for i in xrange(n)] for j in xrange(n)]
        for i, e in enumerate(graph):
            dist[i][i] = 0
            for j in e:
                dist[i][j] = dist[j][i] = 1

        for z in xrange(n):
            for x in xrange(n):
                for y in xrange(n):
                    dist[x][y] = min(dist[x][y], dist[x][z] + dist[z][y])

        dp = [[inf for v in xrange(n + 1)] for s in xrange((1 << n) + 10)]
        for i in xrange(n):
            dp[0][i] = 0

        for s in xrange(1 << n):
            for v in xrange(n):
                if dp[s][v] == inf:
                    continue
                prev = dp[s][v]
                for nv in xrange(n):
                    ns = set_bit(s, nv)
                    if dp[ns][nv] > prev + dist[v][nv]:
                        dp[ns][nv] = prev + dist[v][nv]

        return min(dp[(1 << n) - 1])

sln = Solution()
print sln.shortestPathLength([[1,2,3],[0],[0],[0]]) # 4
print sln.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]) # 4
print sln.shortestPathLength([[1],[0,2,4],[1,3],[2],[1,5],[4]]) # 6

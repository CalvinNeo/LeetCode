class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        inf = 555555555
        dist = [[inf for i in xrange(n)] for j in xrange(n)]

        for (fr, ed, w) in edges:
            dist[fr][ed] = w
            dist[ed][fr] = w

        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    if i == j:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    dist[j][i] = dist[i][j]

        aL = []
        for i in xrange(n):
            t = 0
            for j in xrange(n):
                if dist[i][j] <= distanceThreshold:
                    t += 1
            aL.append(t)
        aLM = min(aL)
        # print dist
        # print aL
        for j in xrange(n - 1, -1, -1):
            if aL[j] == aLM:
                return j

sln = Solution()
print sln.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4) # 3
print sln.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2) # 0
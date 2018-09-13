class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        inf = 5555555555555555
        m = [[inf for i in xrange(N + 1)] for j in xrange(N + 1)]

        for i in xrange(1, N + 1):
            m[i][i] = 0

        for u, v, w in times:
            m[u][v] = w

        dist = [inf] * (N + 1)
        vis = [0] * (N + 1)
        dist[K] = 0

        def rans():
            mx = max(dist[1:])
            if mx == inf:
                return -1
            else:
                return mx

        for i in xrange(1, N + 1):
            min_dis = inf
            min_id = -1
            for j in xrange(1, N + 1):
                if not vis[j] and dist[j] < min_dis:
                    min_dis = dist[j]
                    min_id = j
            if min_id == -1:
                return rans()
            vis[min_id] = 1
            for j in xrange(1, N + 1):
                if not vis[j]:
                    dist[j] = min(dist[j], dist[min_id] + m[min_id][j])
        return rans()

# sln = Solution()
# print sln.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
# print sln.networkDelayTime([[1,2,1]], 2, 2)

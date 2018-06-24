class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        mark = [0 for i in xrange(n)]
        vis = [0 for i in xrange(n)]

        def dfs(s):
            vis[s] = 1
            flag = 0
            # Pay attention to |=
            for i in xrange(len(graph[s])):
                to = graph[s][i]
                if vis[to] == 0:
                    # forward edge
                    vis[to] = 1
                    flag |= dfs(to)
                elif vis[to] == 1:
                    # back edge
                    flag |= 1
                elif vis[to] == 2:
                    flag |= mark[to]
            if flag:
                mark[s] = 1
            vis[s] = 2
            return flag

        for i in xrange(n):
            if not vis[i]:
                dfs(i)
        ans = []
        for i, b in enumerate(mark):
            if not b:
                ans.append(i)
        return ans
sln = Solution()
print sln.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) # 4
print sln.eventualSafeNodes([[]]) # 1
print sln.eventualSafeNodes([[0],[2,3,4],[3,4],[0,4],[]]) # 1
print sln.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) # 4

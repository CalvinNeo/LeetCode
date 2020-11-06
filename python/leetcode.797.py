class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        N = len(graph)
        if N == 0:
            return []
        def dfs(stk, vis):
            cur = stk[-1]
            if cur == N - 1:
                ans.append(stk)
                return 
            for nxt in graph[cur]:
                if not nxt in vis:
                    dfs(stk+[nxt], vis.union(set([nxt])))
        dfs([0], set([0]))
        return ans
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        if n == 0:
            return False

        vis = [0] * n
        def dfs(pos, cur):
            vis[pos] = cur
            for nxt in graph[pos]:
                if vis[nxt] == 0:
                    if dfs(nxt, -cur) == False:
                        return False
                elif vis[nxt] == cur:
                    return False
            return True
        flag = True
        for i in xrange(n):
            if vis[i] == 0:
                flag &= dfs(i, 1)
        return flag

# sln = Solution()
# T F F
# print sln.isBipartite([[1,3], [0,2], [1,3], [0,2]])
# print sln.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])
# print sln.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])

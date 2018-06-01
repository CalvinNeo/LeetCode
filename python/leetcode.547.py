class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if n == 0:
            return 0
        assert(n == len(M[0]))
        tot = 0
        vis = [0] * (n + 1)
        def dfs(s):
            vis[s] = 1
            for i in xrange(n):
                if M[s][i] and not vis[i]:
                    dfs(i)

        for i in xrange(n):
            if not vis[i]:
                dfs(i)
                tot += 1

        return tot

sln = Solution()
print sln.findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]])

print sln.findCircleNum([[1,1,0],
 [1,1,1],
 [0,1,1]])

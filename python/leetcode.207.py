class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        vis = [0] * numCourses

        m = [[] for i in xrange(numCourses)]
        for (x, pre) in prerequisites:
            # pre -> x
            m[pre].append(x)

        def dfs(cur, vis, m):
            vis[cur] = 1
            for next in m[cur]:
                if vis[next] == 0:
                    vis[next] = 1
                    if not dfs(next, vis, m):
                        return False
                elif vis[next] == 1:
                    return False
            vis[cur] = 2
            return True

        for i in xrange(numCourses):
            if vis[i] == 0:
                if not dfs(i, vis, m):
                    return False

        return True

sln = Solution()
print sln.canFinish(2, [[1,0]])
print sln.canFinish(2, [[1,0],[0,1]])


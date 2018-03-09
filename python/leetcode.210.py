from Queue import PriorityQueue
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        degree = [0] * numCourses
        v = [[] for i in xrange(numCourses)]
        for (x, pre) in prerequisites:
            # pre -> x
            v[pre].append(x)
            degree[x] += 1

        q = PriorityQueue()
        for (i, d) in enumerate(degree):
            if d == 0:
                q.put(i)

        ans = []
        while not q.empty():
            cur = q.get()
            print cur
            ans.append(cur)
            for next in v[cur]:
                degree[next] -= 1
                if degree[next] == 0:
                    q.put(next)

        if len(ans) != numCourses:
            return []
        else:
            return ans

sln = Solution()
print sln.findOrder(2, [[1,0]])
print sln.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print sln.findOrder(3, [[0,2],[1,2],[2,0]])
print sln.findOrder(3, [[1,0],[1,2],[0,1]])

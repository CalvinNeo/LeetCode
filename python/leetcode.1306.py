class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """

        n = len(arr)
        vis = [0 for i in range(n)]
        def dfs(i):
            if vis[i]:
                return
            vis[i] = 1
            d = arr[i]
            if 0 <= i + d < n:
                dfs(i + d)
            if 0 <= i - d < n:
                dfs(i - d)

        dfs(start)

        for i in range(n):
            print arr[i], vis[i]
            if arr[i] == 0 and vis[i] == 1:
                return True
        return False

sln = Solution()
sln.canReach([0,3,0,6,3,3,4], 6)
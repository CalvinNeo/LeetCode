class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)

        vis = [0] * n
        self.tot = 0

        def dfs(pos):
            if vis[pos] == 0:
                self.tot += 1
            vis[pos] = 1
            if self.tot == n:
                return True
            for nxt in rooms[pos]:
                if not vis[nxt] and dfs(nxt):
                    return True
            return False
        return dfs(0)

# sln = Solution()
# print sln.canVisitAllRooms([[1],[2],[3],[]])
# print sln.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])

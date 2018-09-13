class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        n = len(image)
        if n == 0:
            return [[]]
        m = len(image[0])
        if m == 0:
            return [[]]

        vis = [[0 for i in xrange(m)] for j in xrange(n)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(x, y):
            DX = [-1, 0, 0, 1]
            DY = [0, -1, 1, 0]
            vis[x][y] = 1
            oc = image[x][y]
            image[x][y] = newColor

            for dx, dy in zip(DX, DY):
                nx, ny = dx + x, dy + y
                if valid(nx, ny) and not vis[nx][ny] and oc == image[nx][ny]:
                    dfs(nx, ny)

        dfs(sr, sc)
        return image

# sln = Solution()
# print sln.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2)
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [0 for i in xrange(n + 2)]
        for i, x in enumerate(books):
            w, h = x
            dp[i] = dp[i-1] + h # new
            totw = w
            toth = h
            for j in xrange(i-1, -1, -1):
                # try [j, i]
                if totw + books[j][0] > shelfWidth:
                    break
                totw += books[j][0]
                toth = max(toth, books[j][1])
                dp[i] = min(dp[i], dp[j-1] + toth)
        return dp[n-1]

    def minHeightShelvesWA(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        if n == 1:
            return books[0]
        books.sort(cmp = lambda x, y: cmp(x[0], x[0]) if x[1] == y[1] else cmp(x[1], y[1]))
        vis = [0 for i in xrange(n)]
        cw = 0
        ch = books[n - 1]
        ans = 0
        for i in xrange(n - 1, -1, -1):
            if vis[i]:
                continue
            ch = books[i][1]
            cw = books[i][0]
            j = i - 1
            while j >= 0:
                if vis[j]:
                    j -= 1
                    continue
                # print "at {} try {} w {}".format(i, j, cw + books[j][0])
                if cw + books[j][0] <= shelfWidth:
                    cw += books[j][0]
                    vis[j] = 1
                j -= 1
            ans += ch
        return ans

sln = Solution()
print sln.minHeightShelves([[1,3],[2,4],[3,2]], 6) # 4
print sln.minHeightShelves([[7,3],[8,7],[2,7],[2,5]], 10) # 15
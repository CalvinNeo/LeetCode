# coding: utf8


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        G = [[] for i in xrange(n)]
        GR = [[] for i in xrange(n)]

        for x, y in richer:
            G[x].append(y)
            # 反向建图
            GR[y].append(x)

        roots = []
        for i in xrange(n):
            if len(G[i]) == 0:
                roots.append(i)

        dp = [None for i in xrange(n)]
        def dfs(cur):
            # 返回子树中quiet最小的index
            if not dp[cur] is None:
                return dp[cur]

            i = cur
            mx = quiet[i]

            if len(GR[cur]) == 0:
                dp[cur] = cur
            else:
                for nxt in GR[cur]:
                    di = dfs(nxt)
                    if quiet[di] < mx:
                        i = di
                        mx = quiet[di]
                dp[cur] = i

            # print "dp[{}] = {}".format(cur, dp[cur])
            return dp[cur]

        for r in roots:
            dfs(r)
        return dp
        # return [quiet[d] for d in dp]
        # return dfs(3)

sln = Solution()
print sln.loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0])
print sln.loudAndRich([[0,2],[1,2]], [1,0,2])

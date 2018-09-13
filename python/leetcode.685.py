class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        in_e = [[] for i in xrange(n + 1)]
        out_e = [[] for i in xrange(n + 1)]
        vis = [0 for i in xrange(n + 1)]

        ind = -1
        outd = -1
        for [f, t] in edges:
            in_e[t].append(f)
            out_e[f].append(t)
            if len(in_e[t]) >= 2:
                ind = t
            if len(out_e[t]) >= 2:
                outd = t

        def find_loop(cur, fr):
            vis[cur] = 1
            for nxt in out_e[cur]:
                if vis[nxt] == 1 and cur != fr:
                    return [cur], nxt
                elif vis[nxt] == 0:
                    res, flag = find_loop(nxt, cur)
                    if res:
                        if flag == None:
                            return res, None
                        else:
                            if flag == cur:
                                return [cur] + res, None
                            else:
                                return [cur] + res, flag
            # print "Set {} to 2".format(cur)
            vis[cur] = 2
            return None, None

        loo, _ = find_loop(1, -1)
        if loo:
            # There is a loop
            if ind != -1:
                for i in in_e[ind]:
                    if i in loo:
                        return [i, ind]
            else:
                aa = None
                for i in xrange(len(loo)):
                    f = loo[i - 1]
                    t = loo[i]
                    if f != outd:
                        if not aa:
                            aa = [f, t]
                        elif edges.index([f, t]) > edges.index(aa):
                            aa = [f, t]
                return aa
        else:
            # There is no loop,
            # So there must be a node which in-deg >= 2
            aa = None
            for f in in_e[ind]:
                if not aa:
                    # print "New aa", aa
                    aa = [f, ind]
                elif edges.index([f, ind]) > edges.index(aa):
                    # print "Update aa", aa
                    aa = [f, ind]
            return aa

sln = Solution()
print sln.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]) # 2, 3
print sln.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]) # 4, 1
print sln.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]) # 2, 1
print sln.findRedundantDirectedConnection([[4,1],[1,2],[2,3],[3,1]]) # 3, 1
print sln.findRedundantDirectedConnection([[5,2],[5,1],[3,1],[3,4],[3,5]]) # 3, 1
print sln.findRedundantDirectedConnection([[6,3],[8,4],[9,6],[3,2],[5,10],[10,7],[2,1],[7,6],[4,5],[1,8]]) # 7, 6
print sln.findRedundantDirectedConnection([[1,5],[3,2],[2,4],[4,5],[5,3]]) # 4, 5
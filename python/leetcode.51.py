class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        bd = [-1] * n
        ans = []
        vis = [False] * n
        def valid(x, y):
            for i in xrange(n):
                if bd[i] != -1:
                    if bd[i] + i == x + y:
                        return False
                    elif i - x == bd[i] - y:
                        return False
            return True
        def solve(i):
            j_choice = zip(*filter(lambda x: x[0] == False, zip(vis, range(n))))[1]
            for j in j_choice:
                if valid(i, j):
                    vis[j] = True
                    bd[i] = j

                    if i == n - 1:
                        output()
                    else:
                        solve(i + 1)

                    vis[j] = False
                    bd[i] = -1
        def output():
            condition = []
            for i in xrange(n):
                pos = bd[i]
                if pos == -1:
                    return
                leading = '.' * max(0, pos)
                trailing = '.' * max(0, n - 1 - pos)
                # print "pos", pos
                # print leading + "Q" + trailing
                condition.append(leading + "Q" + trailing)
            ans.append(condition)
        solve(0)
        return ans

sln = Solution()
print sln.solveNQueens(4)
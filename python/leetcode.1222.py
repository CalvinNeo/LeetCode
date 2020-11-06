#coding: utf8

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        N = 8
        [kx, ky] = king
        ans = []

        x = kx; y = ky

        def valid(x, y):
            return 0 <= x < 8 and 0 <= y < 8

        def check(L):
            x = kx
            y = ky
            while 1:
                if not valid(x, y):
                    break
                if [x, y] in queens:
                    ans.append([x, y])
                    break
                x, y = L(x, y)

        check(lambda x, y: (x - 1, y))
        check(lambda x, y: (x + 1, y))
        check(lambda x, y: (x, y - 1))
        check(lambda x, y: (x, y + 1))

        check(lambda x, y: (x - 1, y - 1))
        check(lambda x, y: (x + 1, y - 1))
        check(lambda x, y: (x - 1, y + 1))
        check(lambda x, y: (x + 1, y + 1))

        return ans

sln = Solution()
print sln.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0])
print sln.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3])
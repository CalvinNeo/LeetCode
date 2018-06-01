class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        i = j = 0
        di = -1; dj = 1
        def inx(x):
            return 0 <= x < n
        def iny(y):
            return 0 <= y < m
        def inrange(x, y):
            return 0 <= x < n and 0 <= y < m
        ans = []
        while True:
            while True:
                # print "add ({}, {})".format(i, j)
                # print matrix[i][j]
                ans.append(matrix[i][j])
                if i == n - 1 and j == m - 1:
                    return ans
                if inrange(i + di, j + dj):
                    i += di
                    j += dj
                else:
                    break
            # print "A i, j", i, j
            if not inx(i + di):
                if iny(j + 1):
                    j += 1
                else:
                    # Consider [[1,2,3], [4,5,6]]
                    i += 1
            elif not iny(j + dj):
                if inx(i + 1):
                    i += 1
                else:
                    j += 1
            di *= -1
            dj *= -1

sln = Solution()
print sln.findDiagonalOrder([[1]])
print sln.findDiagonalOrder([[1,2,3,4,5]])
print sln.findDiagonalOrder([[1],[2],[3],[4],[5]])
print sln.findDiagonalOrder([[1,2], [3,4]])
print sln.findDiagonalOrder([[1,2,3], [4,5,6]])
print sln.findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9]])

def print_mat(mat):
    for l in mat:
        print ' '.join(map(str, l))
    print ""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        """
        1 2
        ---
        3 4
        2
        1
        ---
        5 6
        4
        3 2 1
        ---
        7 8 1
        6   2
        5 4 3
        ---
        7 8 1
        6 9 2
        5 4 3
        ---
        1 2 3
        8 9 4
        7 6 5
        """
        if n == 1:
            return [[1]]
        mat = [[0 for i in xrange(n)] for j in xrange(n)]
        c = 1
        x = -1
        y = -1
        for l in xrange(n, 0, -2):
            l -= 1
            x += 1
            y += 1
            ex = l
            ey = l
            # Important
            if l == 0:
                mat[x][y] = c
                break
            # print_mat(mat)
            if c > n * n:
                break
            mat[x][y : y + ey] = range(c, c + ey)
            y += ey
            c += ey
            # print_mat(mat)
            if c > n * n:
                break
            for i in xrange(x, x + ex):
                mat[i][y] = c + i - x
            x += ex
            c += ex
            # print_mat(mat)
            if c > n * n:
                break
            mat[x][y - ey + 1: y + 1] = range(c + ey - 1, c - 1, -1)
            y -= ey
            c += ey
            # print_mat(mat)
            if c > n * n:
                break
            for i in xrange(x, x - ex, -1):
                mat[i][y] = c - (i - x)
            x -= ex
            c += ex
        return mat
sln = Solution()
print sln.generateMatrix(3)
print_mat( sln.generateMatrix(4) )
print_mat( sln.generateMatrix(2) )
print_mat( sln.generateMatrix(1) )
print_mat( sln.generateMatrix(5) )

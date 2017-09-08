class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        m = len(matrix) 
        n = len(matrix[0])
        i_set, j_set = False, False
        # must before the next m-n loop
        for i in xrange(0, m):
            if matrix[i][0] == 0:
                i_set = True
        for j in xrange(0, n):
            if matrix[0][j] == 0:
                j_set = True

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # print matrix
        # print i_set, j_set

        # must not include line/column 0
        for i in xrange(1, m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0
        for j in xrange(1, n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0
        if i_set:
            for i in xrange(m):
                matrix[i][0] = 0
        if j_set:
            for j in xrange(n):
                matrix[0][j] = 0
        # print matrix
        return
sln = Solution() 
# print sln.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
# print sln.setZeroes([[0,1]])
print sln.setZeroes([[1,1,1],[0,1,2]])
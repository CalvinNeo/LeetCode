class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        def check_start(x, y):
            v = matrix[x][y]
            while valid(x, y):
                if matrix[x][y] != v:
                    # print "False at {} {} ".format(x, y)
                    return False
                x += 1
                y += 1
            return True

        for y in xrange(m):
            if not check_start(0, y):
                return False

        for x in xrange(n):
            if not check_start(x, 0):
                return False

        return True

# sln = Solution()
# print sln.isToeplitzMatrix(matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ])
# print sln.isToeplitzMatrix(matrix = [
#   [1,2],
#   [2,2]
# ])
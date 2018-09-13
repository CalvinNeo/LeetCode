import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False

        col_index = [matrix[i][0] for i in xrange(n)]

        end = bisect.bisect_right(col_index, target)

        for i in xrange(end):
            j = bisect.bisect_left(matrix[i], target)
            if 0 <= j < m and matrix[i][j] == target:
                return True
        return False

sln = Solution()
print sln.searchMatrix([[]], 1)
print sln.searchMatrix([[1]], 1)
print sln.searchMatrix([[2]], 1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import bisect

        m = len(matrix) 
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for i in xrange(m):
            pos = bisect.bisect_left(matrix[i], target)
            if matrix[i][0] > target:
                return False
            print pos
            if pos < n and matrix[i][pos] == target:
                return True
        return False

sln = Solution()
print sln.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3)
print sln.searchMatrix([[]], 3)


# import bisect
# print bisect.bisect_left([[]], 3)
# print bisect.bisect_left([1,2], 3)
# print bisect.bisect_left([1,2], 0)
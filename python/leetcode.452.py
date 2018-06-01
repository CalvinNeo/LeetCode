class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda p: p[0])
        ans = 0
        start_index = 0
        n = len(points)
        while start_index < n:
            # [start_index, end_index)
            end_index = start_index
            border = points[start_index][1]
            while end_index < n and points[end_index][0] <= border:
                border = min(border, points[end_index][1])
                end_index += 1
            ans += 1
            start_index = end_index
        return ans

sln = Solution()
print sln.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
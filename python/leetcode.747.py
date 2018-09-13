class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        mx = None
        mi = -1

        for i, x in enumerate(nums):
            if mx == None:
                mx = x
                mi = i
            elif x > mx:
                prev = mx
                mx = x
                mi = i
            elif x > prev:
                prev = x

        if mx == None:
            return -1
        if prev == None:
            return mi
        elif mx >= 2 * prev:
            return mi
        else:
            return -1

# sln = Solution()
# print sln.dominantIndex([3, 6, 1, 0]) # 1
# print sln.dominantIndex([1, 2, 3, 4]) # -1
# print sln.dominantIndex([1]) # 0
# print sln.dominantIndex([0,0,3,2]) # -1
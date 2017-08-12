class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        def bl(l, r):
            l, r = 0, length - 1
            while l < r:
                m = (l + r) / 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            if  nums[l] == target:
                return l
            elif nums[l] < target:
                return l + 1
            else:
                return l 
        return bl(0, length - 1)
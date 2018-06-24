class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_1 = len(nums)
        n = n_1 - 1
        r = n
        l = 1
        def check(mid):
            lt = 0
            gt = 0
            eq = 0
            for i in nums:
                if i > mid:
                    gt += 1
                elif i < mid:
                    lt += 1
                else:
                    eq += 1
            return lt, gt, eq

        while l < r:
            mid = (l + r) / 2
            lt, gt, eq = check(mid)
            if eq > 1:
                return mid
            should_on_left = mid - 1
            should_on_right = n - mid
            if gt > should_on_right:
                l = mid + 1
            elif lt > should_on_left:
                r = mid - 1
        return l
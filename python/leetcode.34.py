class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        def bl(l, r):
            l, r = 0, length - 1
            while l < r:
                m = (l + r) / 2
                if nums[m] == target:
                    if m > 0 and nums[m - 1] == target:
                        r = m - 1
                    else:
                        return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l if nums[l] == target else -1

        def br(l, r):
            l, r = 0, length - 1
            while l < r:
                m = (l + r) / 2
                print l, r, m
                if nums[m] == target:
                    if m + 1 < length and nums[m + 1] == target:
                        l = m + 1
                    else:
                        return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l if nums[l] == target else -1
        ll = bl(0, length - 1)
        print "======"
        rr = br(0, length - 1)
        return [ll, rr]


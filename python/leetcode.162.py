class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(nums, cur):
            n = len(nums)
            if cur == 0:
                if nums[cur + 1] <= nums[cur]:
                    return 0
                elif nums[cur + 1] > nums[cur]:
                    return -1
            elif cur == n:
                if nums[cur - 1] <= nums[cur]:
                    return 0
                elif nums[cur - 1] > nums[cur]:
                    return 1
            else:
                if nums[cur - 1] <= nums[cur] and nums[cur] >= nums[cur + 1]:
                    return 0
                elif nums[cur - 1] >= nums[cur] >= nums[cur + 1]:
                    return 1
                else:
                    return -1

        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) / 2
            # print l, r, mid
            m = check(nums, mid)
            # print m
            if m == 0:
                return mid
            elif m == -1:
                # too small
                l = mid + 1
            else:
                # too big
                r = mid - 1
        return l

sln = Solution()
# 2 1 2 3 0 2 0 0
print sln.findPeakElement([1,2,3,1])
print sln.findPeakElement([1,2,1])
print sln.findPeakElement([1,2,3,2,1])
print sln.findPeakElement([1,2,3,4,2,1])
print sln.findPeakElement([4,2,1])
print sln.findPeakElement([1,2,3])
print sln.findPeakElement([1])
print sln.findPeakElement([2,1])

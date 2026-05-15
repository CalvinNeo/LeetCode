class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        if n == 1:
            return nums[0]
        while r > 0 and nums[0] == nums[r]:
            r -= 1
        if nums[r] >= nums[0]:
            return nums[0]
        while l <= r:
            mid = (l + r) / 2
            # print "l {} r {} mid {}".format(l, r, mid)
            if nums[mid] > nums[mid + 1]:
                l = mid + 1
                break
            else:
                # Normal, may have ans
                if nums[mid] == nums[l]:
                    # From mid to l is all nums[l]? NO! e.g. (8),8,8,1,8,(8), handle this in pre-test
                    l = mid
                elif nums[mid] > nums[l]:
                    # To the right
                    l = mid
                else:
                    # e.g. [3,1,2]
                    r = mid
        return nums[l]

    def findMinT(self, nums):
        return self.findMin(nums) == min(nums)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        l = 0
        r = n - 1
        if n == 1:
            return nums[0]
        while r > 0 and nums[0] == nums[r]:
            r -= 1
        if nums[r] >= nums[0]:
            return nums[0]

        # find the m that less than m-1
        while l < r:
            # print l, r
            m = (l + r) / 2
            # TODO m-1
            if nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m - 1] <= nums[m]:
                if nums[0] < nums[m]:
                    # 1 (2) 3 Must first wipe out
                    # 1 (2) 3 0 Go right, no include
                    l = m + 1
                elif nums[0] > nums[m]:
                    r = m
                else:
                    # 1 (1) 0
                    l = m + 1
        return nums[l]

sln = Solution()
print sln.findMin([3,1]) # 1
print sln.findMin([1]) # 1
print sln.findMin([3,5,1]) # 1
print sln.findMin([3,1,2]) # 1
print sln.findMin([3,1,1])
print sln.findMin([1,3,5])
print sln.findMin([2,2,2,0,1]) # 0
print sln.findMin([8,8,8,1,8])
print sln.findMin([2,2,2,2,2]) # 2
print sln.findMin([4,5,6,0,1,2]) # 0

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i, l, r = 0, 0, length - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                # print i, "after 0, (l, r) = (%d, %d)" % (l, r), nums
                l+=1
                i+=1
            elif nums[i] == 2:
                # print i, "after 1, (l, r) = (%d, %d)" % (l, r), nums
                nums[i], nums[r] = nums[r], nums[i]
                while l <= r and nums[r] == 2:
                    r-=1
            else:
                i+=1
        return

sln = Solution()
a1 = [0,2,1,1,0,2,1,1,2,0]
# a1 = [0,0,0]
# a1 = [1]
# a1 = [2]
# a1 = [0,1,2,1,0,2,1,0,2,1,1,1,2,0,1]
# a1 = []
# a1 = [1,0]
sln.sortColors(a1)
print a1
            
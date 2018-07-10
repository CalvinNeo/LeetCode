class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        i = 0
        j = 0
        while i < n:
            while nums[i] != i + 1:
                # print i, nums, "swap {}={} and {}={}".format(nums[i] - 1, nums[nums[i] - 1], i, nums[i])
                if nums[nums[i] - 1] == nums[i]:
                    ans.append(nums[i])
                    break
                else:
                    t1 = nums[i] - 1
                    t2 = i
                    nums[t1], nums[t2] = nums[t2], nums[t1]
            i += 1
        dans = list(set(ans))
        return dans
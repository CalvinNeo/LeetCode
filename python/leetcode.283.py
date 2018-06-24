    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zc = len(filter(lambda x: x == 0, nums))
        i = 0
        for j in xrange(n):
            if i > n - zc:
                break
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in xrange(i, n):
            nums[j] = 0
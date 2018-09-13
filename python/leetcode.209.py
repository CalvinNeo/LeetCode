class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        acc = [0] * n
        inf = 5555555555
        self.mi = inf

        for i in xrange(n):
            if i == 0:
                acc[i] = nums[i]
            else:
                acc[i] = acc[i - 1] + nums[i]

        def gs(i, j):
            if i == 0:
                return acc[j]
            else:
                return acc[j] - acc[i - 1]

        def update(i, j):
            if gs(i, j) >= s:
                self.mi = min(self.mi, j - i + 1)
                return 1
            return 0


        i = 0
        j = -1
        cs = 0

        while j < n - 1:
            j += 1
            cs += nums[j]
            while cs >= s:
                self.mi = min(self.mi, j - i + 1)
                cs -= nums[i]
                i += 1

        while cs >= s:
            self.mi = min(self.mi, j - i + 1)
            cs -= nums[i]
            i += 1

        if self.mi == inf:
            return 0
        else:
            return self.mi

sln = Solution()
print sln.minSubArrayLen(7, [2,3,1,2,4,3]) # 2
print sln.minSubArrayLen(4, [1,4,4]) # 1
print sln.minSubArrayLen(15, [5,10,7,4,9,2,8]) # 2
print sln.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]) # 2

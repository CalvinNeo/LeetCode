class Solution(object):
    def jumpTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        length = len(nums)
        l = [sys.maxint] * length
        l[0] = 0
        for i in xrange(0, length):
            s = nums[i]
            for forward in xrange(1, s + 1):
                j = forward + i
                if j < length:
                    l[j] = min(l[j], l[i] + 1)
        return l[length - 1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        length = len(nums)
        l, r = 0, 0
        s = 0
        for i in xrange(length):
            if i > l:
                l = r
                s += 1
            r = max(r, nums[i] + i)
        return s



sln = Solution()
# print sln.jump([2,3,1,1,4])
print sln.jump([1,1,2,1,1])
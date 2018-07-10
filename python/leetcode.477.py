class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        c0 = [0] * 32
        c1 = [0] * 32

        for i, x in enumerate(nums):
            for j in xrange(32):
                if x % 2 == 1:
                    c1[j] += 1
                else:
                    c0[j] += 1
                x /= 2
        ans = 0
        for i in xrange(32):
            ans += c1[i] * c0[i]
        return ans
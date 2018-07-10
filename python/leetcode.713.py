class Solution(object):
    def numSubarrayProductLessThanKTLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # pow_to[i] = prod nums[0, i)
        pow_to = [1 for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            pow_to[i] = pow_to[i - 1] * nums[i - 1]

        ans = 0
        i = 0
        j = 0
        while j < n:
            # prod = product of [i, j]
            prod = pow_to[j + 1] / pow_to[i]
            # print "product between {} and {} = {}".format(i, j, prod)
            if prod >= k:
                i += 1
                if i > j:
                    j = i
            elif prod < k:
                # print "add [{}, {}] to ans {}, now {}".format(i, j, ans, ans + (j - i + 1))
                ans += (j - i + 1)
                j += 1
        return ans

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        ans = 0
        i = 0
        j = 0
        if n < 1:
            return 0
        prod = nums[0]
        while j < n:
            if prod >= k:
                prod /= nums[i]
                i += 1
                if i > j:
                    j = i
                    if j >= n:
                        break
                    prod = nums[i]
            elif prod < k:
                # print "add [{}, {}] to ans {}, now {}".format(i, j, ans, ans + (j - i + 1))
                ans += (j - i + 1)
                j += 1
                if j >= n:
                    break
                prod *= nums[j]
        return ans

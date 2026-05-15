class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        inf = 99999999999
        def maxArr(fr, to):
            if fr == to:
                return nums[fr]
            elif fr > to:
                return -inf
            m = (fr + to) / 2

            left = maxArr(fr, m)
            right = maxArr(m+1, to)

            ans = max(left, right)

            # print "left {} right {}".format(left, right)
            if m + 1 <= to:
                left_max = nums[m]
                left_sum = nums[m]
                for i in xrange(m - 1, fr - 1, -1):
                    left_sum += nums[i]
                    if left_sum > left_max:
                        left_max = left_sum

                right_max = nums[m + 1]
                right_sum = nums[m + 1]
                for i in xrange(m + 2, to + 1):
                    right_sum += nums[i]
                    if right_sum > right_max:
                        right_max = right_sum

                ans = max(ans, right_max + left_max)

            return ans
        return maxArr(0, n-1)

    def maxSubArrayAC(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        m = 0
        acc = 0
        picked = False
        for x in nums:
            if acc + x < 0:
                # restart
                acc = 0
            else:
                acc += x
                picked = True
                m = max(m, acc)
        return m if picked else max(nums)

sln = Solution()
print sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) # 6
print sln.maxSubArray([-1]) # -1
print sln.maxSubArray([-1, -2]) # -1
print sln.maxSubArray([1,2]) # 3
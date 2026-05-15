from collections import deque as dequeue
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        stk = dequeue()
        for i, x in enumerate(nums):
            while stk and stk[0][0] < i - k:
                stk.popleft()

            prev = stk[0][1] if stk else 0
            ans_at_i = x + prev
            # print "ans_at_{} {} prev {} stk {}".format(i, ans_at_i, prev, stk)
            if i == n - 1:
                return ans_at_i
            while stk and stk[-1][1] <= ans_at_i:
                stk.pop()
            stk.append((i, ans_at_i))

    def maxResultTLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [-9999999999 for i in xrange(n + 2)]

        dp[0] = 0
        for i, x in enumerate(nums):
            for j in xrange(i + 1, min(n - 1, i + k) + 1):
                dp[j] = max(dp[j], dp[i] + x)
                # print "i {} j {} dp[i] {} dp[j] {}".format(i, j, dp[i], dp[j])

        return dp[n-1] + nums[n - 1]

sln = Solution()
print sln.maxResult(nums = [1,-1,-2,4,-7,3], k = 2) # 7
print sln.maxResult(nums = [10,-5,-2,4,0,3], k = 3) # 17
print sln.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2) # 0
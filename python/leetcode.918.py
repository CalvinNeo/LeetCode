from collections import deque as dequeue
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = nums + nums
        nn = len(s)

        def maxArr(fr, to):
            if fr == to:
                return s[fr]
            m = (fr + to) / 2

            left = maxArr(fr, m)
            right = maxArr(m+1, to)

            ans = max(left, right)

            # l = 0
            # r = len(stk) - 1
            # while l < r:
            #     m = (l + r) / 2
            #     if stk[m] + n == e:
            #         l = m
            #         break
            #     elif stk[m] + n < e:
            #         l = m + 1
            #     else:
            #         r = m
    def maxSubarraySumCircularAC(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = nums + nums
        nn = len(s)

        S = [0 for j in xrange(nn)]
        for i in xrange(nn):
            S[i] = S[i-1] + s[i]

        ans = max(nums)
        stk = dequeue()
        # print S
        stk.append(0)
        for e, x in enumerate(S):
            while stk and S[stk[-1]] >= x:
                stk.pop()
            while stk and stk[0] + n < e:
                stk.popleft()
            if stk:
                # print "for {}, x {}, stk is {} D {}".format(e, x, map(lambda i: S[i], stk), x - S[stk[0]])
                ans = max(ans, x - S[stk[0]])
            stk.append(e)
        return ans

    def maxSubarraySumCircularTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = nums + nums
        nn = len(s)

        S = [[0 for i in xrange(nn + 1)] for j in xrange(nn + 1)]

        for i in xrange(nn):
            S[i][i] = s[i]

        for i in xrange(nn):
            for j in xrange(i + 1, nn):
                S[i][j] = S[i][j-1] + s[j]

        # print S
        ans = -9999999999
        for b in xrange(nn):
            for l in xrange(n):
                if b+l < nn:
                    # print "update {} {} = {}".format(b, b+l+1, S[b][b+l])
                    ans = max(ans, S[b][b+l])
        return ans

sln = Solution()
print sln.maxSubarraySumCircular([1,-2,3,-2]) # 3
print sln.maxSubarraySumCircular([5,-3,5]) # 10
print sln.maxSubarraySumCircular([-3,-2,-3]) # -2
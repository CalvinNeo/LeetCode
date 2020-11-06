#coding: utf8

class Solution(object):
    def maxSumDivThreeWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = []
        m2 = []
        m0 = 0
        for x in nums:
            if x % 3 == 0:
                m0 += x
            elif x % 3 == 1:
                m1.append(x)
            else:
                m2.append(x)

        m1 = sorted(m1, reverse=True)
        m2 = sorted(m2, reverse=True)

        l = min(len(m1), len(m2))
        s = m0
        for i in xrange(l):
            s += m1[i]
            s += m2[i]

        return s

    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[-1 for j in xrange(3)] for i in xrange(n + 1)]

        def U(i, loc1, loc2):
            # 通过i能从mod=loc1更新到mod-loc2
            if dp[i - 1][loc1] != -1:
                # print "Update nums[{}]={} from loc1 {} to loc2 {} with new value {}".format(i, nums[i], loc1, loc2, nums[i])
                return dp[i - 1][loc1] + nums[i]
            else:
                return max(dp[i - 1][loc2], dp[i][loc2])

        for i in xrange(n):
            if nums[i] % 3 == 0:
                # 尝试更新别人
                n0 = U(i, 0, 0)
                n1 = U(i, 1, 1)
                n2 = U(i, 2, 2)
                dp[i][0] = max(dp[i - 1][0], n0)
                dp[i][1] = max(dp[i - 1][1], n1)
                dp[i][2] = max(dp[i - 1][2], n2)
                # 尝试更新自己
                dp[i][0] = max([dp[i][0], nums[i]])
            elif nums[i] % 3 == 1:
                # 尝试更新别人
                n1 = U(i, 0, 1)
                n2 = U(i, 1, 2)
                n0 = U(i, 2, 0)
                dp[i][0] = max(dp[i - 1][0], n0)
                dp[i][1] = max(dp[i - 1][1], n1)
                dp[i][2] = max(dp[i - 1][2], n2)
                # 尝试更新自己
                dp[i][1] = max([dp[i][1], nums[i]])
            elif nums[i] % 3 == 2:
                # 尝试更新别人
                n2 = U(i, 0, 2)
                n0 = U(i, 1, 0)
                n1 = U(i, 2, 1)
                dp[i][0] = max(dp[i - 1][0], n0)
                dp[i][1] = max(dp[i - 1][1], n1)
                dp[i][2] = max(dp[i - 1][2], n2)
                # 尝试更新自己
                dp[i][2] = max([dp[i][2], nums[i]])

        # for i in xrange(n):
        #     print i, nums[i], dp[i]
        return 0 if dp[n - 1][0] == -1 else dp[n - 1][0]

sln = Solution()
print sln.maxSumDivThree([1,2,3,4,4]) # 12
print sln.maxSumDivThree([4,1,5,3,1]) # 12
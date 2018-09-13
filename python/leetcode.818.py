#coding:utf-8

def high2(x):
    x-=1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x+=1
    return x  

import math
class Solution(object):
    def racecarWA(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [-1 for i in xrange(target + 1)]

        def solve(t):
            if dp[t] != -1:
                return dp[t]
            top_i = int(math.ceil(math.log(t + 1, 2) - 1))
            ops = top_i + 1
            max_reach = 2 ** ops - 1
            # print "t {} top_i {}".format(t, top_i)
            if max_reach == t:
                # n * A
                dp[t] = ops
            else:
                # max_reach > target:
                dp[t] = ops + 1 + solve(max_reach - t)
                print "t {} goback ans = {} ops {} rest {} = {}".format(t, dp[t], ops, max_reach - t, solve(max_reach - t))
                for i in xrange(top_i):
                    ops_i = i + 1
                    part_reach = 2 ** ops_i - 1
                    # 凭啥立即就回来？
                    dp[t] = min(ops_i + 2 + solve(t - part_reach), dp[t])
            return dp[t]

        ans = solve(target)
        return ans

    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = {}

        def solve(t):
            if t in dp:
                return dp[t]
            top_i = int(math.ceil(math.log(t + 1, 2) - 1))
            ops = top_i + 1
            max_reach = 2 ** ops - 1
            # print "t {} top_i {}".format(t, top_i)
            if max_reach == t:
                # n * A
                dp[t] = ops
            else:
                # max_reach > target:
                dp[t] = ops + 1 + solve(max_reach - t)
                # print "t {} goback ans = {} ops {} rest {} = {}".format(t, dp[t], ops, max_reach - t, solve(max_reach - t))
                for i in xrange(top_i):
                    # 走到ops-1步保证不超过，往回走i步
                    goback = t - 2 ** (ops - 1) + 2 ** i
                    more_need = solve(goback)
                    tot_need = ops + 1 + i + more_need
                    # print "t {} top_i = {}, i = {}, more_need = solve({}) = {}, tot_need = {}".format(t, top_i, i, goback, more_need, tot_need)
                    dp[t] = min(tot_need, dp[t])
            return dp[t]

        ans = solve(target)
        return ans
        
# sln = Solution()
# print sln.racecar(2) # 4
# print sln.racecar(3) # 2
# print sln.racecar(1) # 1
# print sln.racecar(6) # 5
# print sln.racecar(5) # 7 AARRAARA, AARARAA

# t 2 solve(1) = nn 4
# t 5 solve(2) = nn 8
# t 5 solve(3) = nn 7
# 7


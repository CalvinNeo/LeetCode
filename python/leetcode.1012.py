#coding: utf8

class Solution(object):
    def numDupDigitsAtMostNWA(self, N):
        """
        :type N: int
        :rtype: int
        """
        def make_num(x):
            ans = []
            while x:
                ans.append(x % 10)
                x /= 10
            if ans == []:
                ans = [0]
            return ans

        def M(ok, v, no0):
            return str(v) + "_" + str(ok) + "_" + str(no0)
        def RM(x):
            [v, ok, no0] = map(int, x.split("_"))
            return v, ok, no0

        if N <= 0:
            return 0
        nums = make_num(N)
        length = len(nums)
        self.dp = []

        def dfs(cur, status, flag, nums):
            # flag表示在遍历当前pos位时，比pos位低的[0..pos−1]位
            if cur == -1:
                # 如果到达最深层，check是否继续满足题目中的性质
                return RM(status)[1] and (RM(status)[2])

            # if (not flag) and status in self.dp[cur]:
            #     # 如果此层能够取满，那查看能不能复用存储的结果
            #     return self.dp[cur][status]

            ans = 0
            end = nums[cur] + 1 if flag else 10 # 如果flag为true就是不自由的，end只能取到nums[cur]

            st = 1 if cur == length - 1 else 0
            for i in xrange(0, end):
                # 如果最终结果与前缀的结果满足and或者or的性质，这里还可以剪枝
                newflag = flag and (i == end - 1) # 下一层的flag，注意要同时满足两个条件才会有限制
                prev, ok, no0 = RM(status)
                new_no0 = no0 | int(i != 0) # True表示没有前置的0
                if i == prev and new_no0:
                    delta = dfs(cur - 1, M(1, i, new_no0), newflag, nums)
                    if cur >= 1:
                        print "SAME num[{}]={} prev {} ok {} delta = {}".format(cur, i, prev, ok, delta)
                    ans += delta
                else:
                    delta = dfs(cur - 1, M(ok, i, new_no0), newflag, nums)
                    if cur >= 1:
                        print "NO SAME num[{}]={} prev {} ok {} delta = {}".format(cur, i, prev, ok, delta)
                    ans += delta
                if cur >= 2:
                    print "num[{}]={} prev {} ok {} ans = {}".format(cur, i, prev, ok, ans)

            if not flag:
                # 只保存任何层取满[0..9]的结果
                self.dp[cur][status] = ans
            return ans

        self.dp = [{} for y in xrange(length)]
        ans = dfs(length - 1, M(0, -1, 1), True, nums)
        return ans


    def numDupDigitsAtMostNWA2(self, N):
        """
        :type N: int
        :rtype: int
        """
        def make_num(x):
            ans = []
            while x:
                ans.append(x % 10)
                x /= 10
            if ans == []:
                ans = [0]
            return ans

        def M(duplicate, v, lead):
            return str(v) + "_" + str(int(duplicate)) + "_" + str(int(lead))
        def RM(x):
            [v, duplicate, lead] = map(int, x.split("_"))
            return v, duplicate, lead

        if N <= 0:
            return 0
        nums = make_num(N)
        length = len(nums)
        self.dp = []

        def dfs(cur, status, flag, nums):
            # flag表示在遍历当前pos位时，比pos位低的[0..pos−1]位
            if cur == -1:
                # 如果到达最深层，check是否继续满足题目中的性质
                return RM(status)[1]

            # if (not flag) and status in self.dp[cur]:
            #     # 如果此层能够取满，那查看能不能复用存储的结果
            #     return self.dp[cur][status]

            cnt = 0
            end = nums[cur] + 1 if flag else 10 # 如果flag为true就是不自由的，end只能取到nums[cur]

            st = 1 if cur == length - 1 else 0
            for d in xrange(0, end):
                # 如果最终结果与前缀的结果满足and或者or的性质，这里还可以剪枝
                nextstat, duplicate, lead = RM(status)

                next_dup = duplicate
                if flag and d == 0:
                    pass
                else:
                    nextstat |= (1 << d)
                    next_dup = next_dup or (nextstat & (1 << d))

                cnt += dfs(cur - 1, M(next_dup, nextstat, (lead and d == 0)), flag and (d == end - 1), nums)

            if not flag:
                # 只保存任何层取满[0..9]的结果
                self.dp[cur][status] = cnt
            return cnt

        self.dp = [{} for y in xrange(length)]
        cnt = dfs(length - 1, M(0, 0, 1), True, nums)
        return cnt

    def numDupDigitsAtMostNTLE(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dfs(nums, cur, status, duplicate, lead, flag):
            if (cur == -1):
                return 1 if duplicate else 0
            # lead 是否有前导0
            # duplicate 是否已经看到重复
            # flag 是否能取到限制

            # print "cur {} status {} duplicate {} lead {} flag {}".format(cur, status, duplicate, lead, flag)
            if(self.dp[cur][status][int(duplicate)][int(lead)][int(flag)] != -1):
                return self.dp[cur][status][int(duplicate)][int(lead)][int(flag)]

            end = nums[cur] + 1 if flag else 10
            cnt = 0;
            for d in xrange(0, end):
                next_stat = status
                next_dup = duplicate
                if(lead and d == 0):
                    # 如果有前导0的，就不管
                    pass
                else:
                    # 否则更新前面有哪些数字
                    next_stat |= 1 << d
                    next_dup = next_dup or bool(status & (1 << d))
                cnt += dfs(nums, cur - 1, next_stat, next_dup,
                        lead and d == 0, flag and d == end - 1)
            
            self.dp[cur][status][int(duplicate)][int(lead)][int(flag)] = cnt
            return cnt

        nums = []
        self.dp = [[[[[-1 for m in xrange(2)] for l in xrange(2)] for k in xrange(2)] for j in xrange(2 ** 10)] for i in xrange(10)]
        while(N):
            nums.append(N % 10)
            N /= 10
        length = len(nums)
        return dfs(nums, length - 1, 0, False, True, True)

    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dfs(nums, cur, status, duplicate, lead, flag):
            if (cur == -1):
                return 1 if duplicate else 0
            # lead 是否有前导0
            # duplicate 是否已经看到重复
            # flag 是否能取到限制

            # print "cur {} status {} duplicate {} lead {} flag {}".format(cur, status, duplicate, lead, flag)
            if (not flag) and (self.dp[cur][status][int(duplicate)][int(lead)] != -1):
                return self.dp[cur][status][int(duplicate)][int(lead)]

            end = nums[cur] + 1 if flag else 10
            cnt = 0;
            for d in xrange(0, end):
                next_stat = status
                next_dup = duplicate
                if(lead and d == 0):
                    # 如果有前导0的，就不管
                    pass
                else:
                    # 否则更新前面有哪些数字
                    next_stat |= 1 << d
                    next_dup = next_dup or bool(status & (1 << d))
                cnt += dfs(nums, cur - 1, next_stat, next_dup,
                        lead and d == 0, flag and d == end - 1)
            
            if not flag:
                self.dp[cur][status][int(duplicate)][int(lead)] = cnt
            return cnt

        nums = []
        self.dp = [[[[-1 for l in xrange(2)] for k in xrange(2)] for j in xrange(2 ** 10)] for i in xrange(10)]
        while(N):
            nums.append(N % 10)
            N /= 10
        length = len(nums)
        return dfs(nums, length - 1, 0, False, True, True)

sln = Solution()
print sln.numDupDigitsAtMostN(10) # 0
print sln.numDupDigitsAtMostN(19) # 1
print sln.numDupDigitsAtMostN(20) # 1
print sln.numDupDigitsAtMostN(30) # 2
print sln.numDupDigitsAtMostN(90) # 8
print sln.numDupDigitsAtMostN(100) # 10
print sln.numDupDigitsAtMostN(1000) # 262
# print sln.numDupDigitsAtMostN(1001) # 263
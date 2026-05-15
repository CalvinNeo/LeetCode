class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        m = len(group)

        dp = [[[-1 for k in range(minProfit + 1)] for j in xrange(n+1)] for i in xrange(m+1)]

        MOD = 10 ** 9 + 7

        def dfs(i, restPeople, restProfit):
            if i < 0:
                return 0

            if dp[i][restPeople][restProfit] != -1:
                return dp[i][restPeople][restProfit]

            if i == 0:
                ans = 0
                if restPeople >= group[0] and profit[0] >= restProfit:
                    ans += 1
                if restProfit <= 0:
                    ans += 1
                dp[i][restPeople][restProfit] = ans
                return ans

            restPeopleNew = restPeople - group[i]
            if restProfit <= 0:
                ans = 0
                if restPeople >= group[i]:
                    ans += dfs(i-1, restPeople - group[i], restProfit)
                ans += dfs(i-1, restPeople, restProfit)
                dp[i][restPeople][restProfit] = ans
                return ans

            restProfitNew = restProfit - profit[i]
            # print "PPP i {}/{}, restPeople {}/{}, restProfit {}/{}, restPeopleNew {}, restProfitNew {}".format(i, m, restPeople, n, restProfit, minProfit, restPeopleNew, restProfitNew)
            # we don't take this one
            dp[i][restPeople][restProfit] = dfs(i-1, restPeople, restProfit)
            if restPeopleNew >= 0:
                # we take this one
                if restProfitNew < 0:
                    restProfitNew = 0

                dp[i][restPeople][restProfit] += dfs(i-1, restPeopleNew, restProfitNew)
                dp[i][restPeople][restProfit] %= MOD
            
            # print "i {}/{}, restPeople {}/{}, restProfit {}/{}, restPeopleNew {}, restProfitNew {}, ans = {}".format(i, m, restPeople, n, restProfit, minProfit, restPeopleNew, restProfitNew, dp[i][restPeople][restProfit])
            return dp[i][restPeople][restProfit]

        return dfs(m-1, n, minProfit)

    def profitableSchemesWA(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        m = len(group)

        dp = [[[-1 for k in range(minProfit + 1)] for j in xrange(n+1)] for i in xrange(m+1)]

        MOD = 10 ** 9 + 7

        # We can't just assume here, since there may be not enough people
        for i in xrange(m+1):
            for p in xrange(n+1):
                dp[i][p][0] = (2 ** (i + 1)) % MOD

        def dfs(i, restPeople, restProfit):
            if i < 0:
                return 0
            if i == 0:
                ans = 0
                if restPeople >= group[0] and profit[0] >= restProfit:
                    ans += 1
                if restProfit <= 0:
                    ans += 1
                return ans
            if dp[i][restPeople][restProfit] != -1:
                return dp[i][restPeople][restProfit]

            restPeopleNew = restPeople - group[i]
            restProfitNew = restProfit - profit[i]
            # print "PPP i {}/{}, restPeople {}/{}, restProfit {}/{}, restPeopleNew {}, restProfitNew {}".format(i, m, restPeople, n, restProfit, minProfit, restPeopleNew, restProfitNew)
            # we don't take this one
            dp[i][restPeople][restProfit] = dfs(i-1, restPeople, restProfit)
            if restPeopleNew >= 0:
                # we take this one
                if restProfitNew < 0:
                    restProfitNew = 0

                dp[i][restPeople][restProfit] += dfs(i-1, restPeopleNew, restProfitNew)
                dp[i][restPeople][restProfit] %= MOD
            
            # print "i {}/{}, restPeople {}/{}, restProfit {}/{}, restPeopleNew {}, restProfitNew {}, ans = {}".format(i, m, restPeople, n, restProfit, minProfit, restPeopleNew, restProfitNew, dp[i][restPeople][restProfit])
            return dp[i][restPeople][restProfit]

        return dfs(m-1, n, minProfit)

sln = Solution()
print sln.profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3]) # 2
print sln.profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]) # 7
print sln.profitableSchemes(n = 64, minProfit = 0, group = [80, 40], profit = [88, 88]) # 2
print sln.profitableSchemes(n = 100, minProfit = 1, group = [60,36,37,80,66,96,61,14,43,18,35,98,38,49,66,83,90,60,80,88,14,44,65,78,31,55,79,46,1,90,74,53,62,68,24,37,73,56,37,48,86,51,56,66,51,72,29,34,96,57,84,13,99,69,47,45,55,58,31,60,94,9,60,72,27,59,95,100,40,98,77,10,62,78,32,100,51,96,52,85,40,61,31,8,20,75,32,78,53,67,22,2,40,29,74,68,2,46,3,93], profit = [2,2,0,0,2,2,0,1,2,2,2,2,2,1,0,0,2,1,2,0,1,1,2,2,0,0,2,0,2,0,1,1,0,0,0,1,2,2,0,2,2,1,0,1,2,0,1,0,2,1,2,2,2,0,1,1,0,0,0,2,1,2,1,0,2,1,1,1,0,1,1,2,2,0,1,1,1,1,1,0,1,0,1,2,0,0,1,2,1,1,0,1,2,2,1,1,0,0,0,1]) # 

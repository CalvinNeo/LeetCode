class Solution(object):
    def numberOfArithmeticSlicesTLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        self.ans = 0
        def dfs(i, last, dif, l):
            if i == n:
                if l >= 3:
                    self.ans += 1
                return
            if l == 0:
                # choose head
                dfs(i + 1, None, None, 0)
                dfs(i + 1, A[i], None, 1)
            elif l == 1:
                # choose dif
                dfs(i + 1, last, None, 1)
                dfs(i + 1, A[i], A[i] - last, 2)
            else:
                # normal
                dfs(i + 1, last, dif, l)
                if dif + last == A[i]:
                    dfs(i + 1, A[i], dif, l + 1)

        dfs(0, None, None, 0)
        return self.ans

    def numberOfArithmeticSlices1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        self.dp = [[-1 for i in xrange(n + 1)] for j in xrange(n + 1)]
        def dfs(i, fst, snd, last, l):
            ans = 0
            if i == n:
                if l >= 3:
                    return 1
                return 0
            if l == 0:
                ans += dfs(i + 1, None, None, None, 0)
                ans += dfs(i + 1, i, None, i, 1)
            elif l == 1:
                ans += dfs(i + 1, fst, None, last, 1)
                # ans += dfs(i + 1, fst, i, i, 2)
                if self.dp[fst][i] == -1:
                    self.dp[fst][i] = dfs(i + 1, fst, i, i, l + 1)
                    print "By SEARCH, fst {}, i {}, self.dp[fst][i] {}, l {}".format( fst, i, self.dp[fst][i], l )
                else:
                    print "By MEM, fst {}, i {}, self.dp[fst][i] {}, l {}".format( fst, i, self.dp[fst][i], l )
                ans += self.dp[fst][i]
            else:
                ans += dfs(i + 1, fst, snd, last, l) 
                if A[i] - A[last] == A[snd] - A[fst]:
                    if self.dp[last][i] == -1:
                        self.dp[last][i] = dfs(i + 1, last, i, i, l + 1)
                        print "By SEARCH, last {}, i {}, self.dp[last][i] {}, l {}".format( last, i, self.dp[last][i], l )
                    else:
                        print "By MEM, last {}, i {}, self.dp[last][i] {}, l {}".format( last, i, self.dp[last][i], l )
                    ans += self.dp[last][i]
            return ans

        ans = dfs(0, None, None, None, 0)
        return ans

    def numberOfArithmeticSlices2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        self.dp = [[-1 for i in xrange(n + 1)] for j in xrange(n + 1)]
        def dfs(i, fst, snd, l):
            ans = 0
            if i == n:
                if l >= 3:
                    return 1
                return 0
            if l == 0:
                ans += dfs(i + 1, n, n, 0)
                ans += dfs(i + 1, i, n, 1)
            elif l == 1:
                ans += dfs(i + 1, fst, n, l)
                # ans += dfs(i + 1, fst, i, 2)
                if self.dp[fst][i] == -1:
                    self.dp[fst][i] = dfs(i + 1, fst, i, l + 1)
                    print "By SEARCH, fst {}, i {}, self.dp[fst][i] {}, l {}".format( fst, i, self.dp[fst][i], l )
                else:
                    print "By MEM, fst {}, i {}, self.dp[fst][i] {}, l {}".format( fst, i, self.dp[fst][i], l )
                ans += self.dp[fst][i]
            else:
                ans += dfs(i + 1, fst, snd, l)
                if A[i] - A[snd] == A[snd] - A[fst]:
                    if self.dp[snd][i] == -1:
                        self.dp[snd][i] = dfs(i + 1, snd, i, l + 1)
                        print "By SEARCH, snd {}, i {}, self.dp[snd][i] {}, l {}".format( snd, i, self.dp[snd][i], l )
                    else:
                        print "By MEM, snd {}, i {}, self.dp[snd][i] {}, l {}".format( snd, i, self.dp[snd][i], l )
                    ans += self.dp[snd][i]
            return ans

        ans = dfs(0, n, n, 0)
        return ans


    def numberOfArithmeticSlicesTLE2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[0 for i in xrange(n + 1)] for j in xrange(n + 1)]
        for prev in xrange(0, n):
            for fst in xrange(prev + 1, n):
                for snd in xrange(fst + 1, n):
                    if A[prev] - A[fst] == A[fst] - A[snd]:
                        # total_len = dp[prev][fst] + 2
                        # print prev, fst, snd
                        dp[fst][snd] += (dp[prev][fst] + 1)
        ans = 0
        for fst in xrange(n):
            for snd in xrange(fst + 1, n):
                ans += dp[fst][snd]
        return ans

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[0 for i in xrange(n + 1)] for j in xrange(n + 1)]
        for prev in xrange(0, n):
            for fst in xrange(prev + 1, n):
                for snd in xrange(fst + 1, n):
                    if A[prev] - A[fst] == A[fst] - A[snd]:
                        # total_len = dp[prev][fst] + 2
                        # print prev, fst, snd
                        dp[fst][snd] += (dp[prev][fst] + 1)
        ans = 0
        for fst in xrange(n):
            for snd in xrange(fst + 1, n):
                ans += dp[fst][snd]
        return ans

sln = Solution()
print sln.numberOfArithmeticSlices([]) # 0
print sln.numberOfArithmeticSlices([2,2,3,4]) # 2
print sln.numberOfArithmeticSlices([0, 1, 2, 2, 2]) # 4
print sln.numberOfArithmeticSlices([2, 4, 6]) # 1
print sln.numberOfArithmeticSlices([2, 4, 6, 8, 10]) # 7
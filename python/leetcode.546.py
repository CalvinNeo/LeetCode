def make_acc(L):
    prev = None
    acc = 0
    ans = []
    for x in L:
        if x != prev:
            if prev != None:
                ans.append((prev, acc))
            prev = x
            acc = 1
        else:
            acc += 1
    if prev != None:
        ans.append((prev, acc))
    return ans

class Solution(object):
    def removeBoxesTLE(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def dfs(L):
            if len(L) == 1:
                return L[0][1] ** 2
            elif len(L) == 0:
                return 0

            n = len(L)
            ch = 0
            for i in xrange(n):
                if i-1>=0 and i+1<n and L[i-1][0] == L[i+1][0]:
                    ch = max(ch, L[i][1] ** 2 + dfs(L[:i-1] + [(L[i-1][0], L[i-1][1]+L[i+1][1])] + L[i+2:]))
                else:
                    ch = max(ch, L[i][1] ** 2 + dfs(L[:i] + L[i+1:]))
            return ch

        L = make_acc(boxes)
        # print L
        return dfs(L)

    def removeBoxesWA(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        L = make_acc(boxes)
        n = len(L)

        dp = [[[-1 for i in xrange(n)] for j in xrange(n)] for k in xrange(n)]

        def dfs(l, r):
            if l > r:
                return 0

            ch = 0
            for take in xrange(l, r + 1):
                delta = 0
                part = 0

                if take-1>=l and take+1<=r and L[take+1][0] == L[take-1][0]:
                    i = take + 1
                    acc = 0
                    acc += L[take-1][1]
                    while take-1 >= l and i <= r and L[i][0] == L[take-1][0]:
                        acc += L[i][1]
                        i += 1

                    delta += acc ** 2
                    part += dfs(l, take - 2)
                    part += dfs(i, r)

                else:
                    delta += L[take][1] ** 2
                    part += dfs(l, take - 1)
                    part += dfs(take + 1, r)

                ch = max(ch, delta + part)

            return ch

        print L
        return dfs(0, n - 1)


    def removeBoxesWA2(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        L = make_acc(boxes)
        n = len(L)

        dp = [[[-1 for i in xrange(n)] for j in xrange(n)] for k in xrange(n)]

        def dfs(l, r):
            if l > r:
                return 0

            ch = 0
            for take in xrange(l, r + 1):
                if dp[l][r][take] == -1:
                    part = 0
                    lpart = dfs(l, take - 1)
                    for i in xrange(take, r + 1):
                        # l take i r
                        mpart = 0
                        c = 0
                        prev = None
                        for j in xrange(take, i + 1):
                            if prev != None and prev == L[j][0]:
                                c += L[j][1]
                            else:
                                mpart += c ** 2
                                c = L[j][1]
                                prev = L[j][0]
                        if c:
                            mpart += c ** 2
                        rpart = dfs(i + 1, r)

                        if l == 0 and r == 2 and i == 1 and take == 1:
                            print "===>", lpart, mpart, rpart  
                            print "l {} i {} r {} take {}".format(l, i, r, take)
                        part_upd = lpart + mpart + rpart
                        part = max(part, part_upd)

                    dp[l][r][take] = part

                ch = max(ch, dp[l][r][take])
            return ch

        print L
        # print dp[0][2][1]
        return dfs(0, n - 1)


    def removeBoxesWA3(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        L = make_acc(boxes)
        n = len(L)

        dp = [[[-1 for i in xrange(n)] for j in xrange(n)] for k in xrange(n)]

        def dfs(l, r):
            if l > r:
                return 0
            elif l == r:
                return L[l][1] ** 2

            ch = 0
            for take in xrange(l + 1, r + 1):
                if dp[l][r][take] == -1:
                    part = 0
                    for i in xrange(take, r + 1):
                        # if l == 0 and r == n - 1:
                        #     print "============"
                        # l take i r
                        mpart = dfs(take, i)

                        # if l == 0 and r == n - 1:
                        #     print "mpart[{},{}] {}".format(take, i, mpart)

                        lpart, rpart = 0, 0

                        j = i + 1
                        if j <= r and L[j][0] == L[take-1][0]:
                            # Do concat
                            c = L[take-1][1]
                            while j <= r and L[j][0] == L[take-1][0]:
                                c += L[j][1]
                                j += 1
                            rpart += c ** 2
                            rpart += dfs(j, r)
                            # if l == 0 and r == n - 1:
                            #     print "rpart(merge)[{},{}] {} c {}".format(i+1, r, rpart, c)
                        else:
                            rpart += dfs(j, r)
                            # if l == 0 and r == n - 1:
                            #     print "rpart(normal)[{},{}] {}".format(i+1, r, rpart)

                        if j == i + 1:
                            lpart = dfs(l, take - 1)
                            # if l == 0 and r == n - 1:
                            #     print "lpart[{},{}] {}".format(l, take - 1, lpart)
                        else:
                            lpart = dfs(l, take - 2)
                            # if l == 0 and r == n - 1:
                                # print "lpart[{},{}] {}".format(l, take - 2, lpart)

                        # print lpart , mpart , rpart
                        new_part = lpart + mpart + rpart
                        part = max(part, new_part)

                    dp[l][r][take] = part

                ch = max(ch, dp[l][r][take])
            return ch

        # print L
        # dfs(0, n - 1)
        # print max(dp[1][4])
        return dfs(0, n - 1)
        # return dfs(1, 2)

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        L = make_acc(boxes)
        nn = len(boxes)
        n = len(L)

        dp = [[[-1 for i in xrange(nn)] for j in xrange(n)] for k in xrange(n)]

        def dfs(l, r, k):
            if l > r:
                return 0
            # if k >= n:
            #     return 0
            # if k >= n:
                # k = n - 1

            if dp[l][r][k] != -1:
                return dp[l][r][k]

            dp[l][r][k] = dfs(l, r - 1, 0) + (k + L[r][1]) ** 2
            for i in xrange(l, r):
                if L[i][0] == L[r][0]:
                    dp[l][r][k] = max(dp[l][r][k], dfs(l, i, k + L[r][1]) + dfs(i + 1, r - 1, 0))

            return dp[l][r][k]

        return dfs(0, n - 1, 0)

# sln = Solution()
# print sln.removeBoxes([1, 2, 2, 1]) # 8
# print sln.removeBoxes([1, 2, 2, 2]) # 10
# print sln.removeBoxes([1, 2, 2, 2, 1]) # 13
# print sln.removeBoxes([1, 2, 3, 3, 3, 2, 1]) # 17
# print sln.removeBoxes([2, 3, 3, 3, 2, 1]) # 14
# print sln.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) # 23
# print sln.removeBoxes([1, 3, 2, 2, 2, 3, 3, 1]) # 22
# print sln.removeBoxes([1,2,3,4,5,6,7,8,9,10]) # 10
# print sln.removeBoxes([1,2,3]) # 3
# print sln.removeBoxes([1, 2, 2, 2, 1, 3, 1]) # 19
# print sln.removeBoxes([1,1,1,1,1,1,1,1,1,1,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) # 14

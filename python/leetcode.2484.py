class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        MOD = 10**9+7
        dp = [[[-1 for i in xrange(n)] for j in xrange(n)] for l in xrange(7)]
        REST = 3
        # equal to s[n-1]
        dp1 = [0 for i in xrange(n)]
        # equal to s[0]
        dp2 = [0 for i in xrange(n)]
        flag = False
        for i in xrange(0, n-1):
            if flag:
                dp1[i] = 1
            else:
                if s[i] == s[n-1]:
                    flag = True
                    dp1[i] = 1
        flag = False
        for i in xrange(n-1, 0, -1):
            if flag:
                dp2[i] = 1
            else:
                if s[i] == s[0]:
                    flag = True
                    dp2[i] = 1

        def c(deep, l, r, rest):
            # count of palind of [0,l] and [r,n-1]
            if l > r:
                # print "Z2"
                return 0
            if rest < 0:
                # print "Z3"
                return 0

            if rest == 0:
                if l < 0 or l >= n:
                    print "    " * deep, "f Left {} Right {} rest {} HIT".format(l, r, rest)
                    return 1
                if r < 0 or r >= n:
                    print "    " * deep, "f Left {} Right {} rest {} HIT".format(l, r, rest)
                    return 1 
            if l < 0 or l >= n:
                # print "Z"
                return 0
            if r < 0 or r >= n:
                # print "Z1"
                return 0

            if dp[rest][l][r] != -1:
                return dp[rest][l][r]
            print "    " * deep, "===<<< start dp[{}][{}][{}]".format(rest, l, r)
            dp[rest][l][r] = 0
            if s[l] == s[r]:
                print "    " * deep, "side Left {} Right {} rest {} REST {}".format(l, r, rest, REST)
                dp[rest][l][r] += c(deep + 1, l-1, r+1, rest-2) % MOD

            # pick 1
            if rest == REST:
                # print "mid Left {} Right {} rest {}".format(l, r, rest)
                L = c(deep + 1, l-1, r, rest-1)
                dp[rest][l][r] += L % MOD
                print "    " * deep, "try mid Left {} Right {} rest {} L1 {} now dp[rest][l][r] {}".format(l-1, r, rest-1, L, dp[rest][l][r])
                R = c(deep + 1, l, r+1, rest-1)
                dp[rest][l][r] += R % MOD
                print "    " * deep, "try mid Left {} Right {} rest {} R1 {} now dp[rest][l][r] {}".format(l, r+1, rest-1, R, dp[rest][l][r])
            # pick 0
            # L = c(deep + 1, l-1, r, rest)
            # dp[rest][l][r] += L % MOD
            # print "    " * deep, "try negect Left {} Right {} rest {} REST {} L0 {} now dp[rest][l][r] {}".format(l-1, r, rest, REST, L, dp[rest][l][r])
            # R = c(deep + 1, l, r+1, rest)
            # dp[rest][l][r] += R % MOD
            # print "    " * deep, "try negect Left {} Right {} rest {} REST {} R0 {} now dp[rest][l][r] {}".format(l, r+1, rest, REST, R, dp[rest][l][r])
            # dp[rest][l][r] -= c(deep + 1, l-1, r+1, rest) % MOD
            dp[rest][l][r] += c(deep + 1, l-1, r+1, rest) % MOD
            print "    " * deep, "===> set dp[{}][{}][{}] = {}".format(rest, l, r, dp[rest][l][r])
            return dp[rest][l][r]

        ans = 0
        for i in xrange(0, n-1):
            print "===================="
            ans = max(ans, c(0, i, i+1, REST))
        return ans

    def countPalindromesWA(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        MOD = 10**9+7
        dp = [[[-1 for i in xrange(n)] for j in xrange(n)] for l in xrange(7)]
        def c(l, r, rest):
            # count of palind of [0,l] and [r,n-1]
            if l < 0 or l >= n:
                return 0
            if r < 0 or r >= n:
                return 0
            if l > r:
                return 0
            if rest < 0:
                return 0

            if l == r:
                if rest == 0:
                    print "f l {} r {} rest {} HIT".format(l, r, rest)
                    return 1
                else:
                    return 0
            # if l + 1 == r:
            #     if s[l] == s[r] and rest == 2:
            #         print "f2 l {} r {} rest {} HIT".format(l, r, rest)
            #         return 1
            #     else:
            #         print "f2 l {} r {} rest {} NOHIT".format(l, r, rest)
            #         return 0
            # if l == r:
            #     if rest == 0:
            #         print "f1 l {} r {} rest {} HIT".format(l, r, rest)
            #         return 1
            #     else:
            #         print "f1 l {} r {} rest {} NOHIT".format(l, r, rest)
            #         return 0

            if dp[rest][l][r] != -1:
                return dp[rest][l][r]

            dp[rest][l][r] = 0
            if s[l] == s[r]:
                print "eq l {} r {} rest {}".format(l, r, rest)
                # pick 2
                dp[rest][l][r] += c(l+1, r-1, rest-2) % MOD
            else:
                print "neq l {} r {} rest {}".format(l, r, rest)

            # pick 1
            if rest == 1:
                print "=== l {} r {} rest {}".format(l, r, rest)
                dp[rest][l][r] += (c(l-1, r+1, rest-1) * (r - l - 1)) % MOD
            # pick 0
            dp[rest][l][r] += c(l+1, r, rest) % MOD
            dp[rest][l][r] += c(l, r-1, rest) % MOD
            return dp[rest][l][r]

        ans = c(0, n-1, 3)
        print dp[5]
        return ans

sln = Solution()
# print sln.countPalindromes("103301") # 2
# print sln.countPalindromes("0000000")# 21 
print sln.countPalindromes("1221") # 2

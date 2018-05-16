def setbit(x, i):
    return (x | (1 << i)) & 0xffffffff

def unsetbit(x, i):
    return x & ((~(1 << i)) & 0xffffffff) & 0xffffffff

def getbit(x, i):
    return (x >> i) & 1 & 0xffffffff

class Solution(object):
    def canIWinWA(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def dfs(sgn, choices, total, alpha, beta, deep):
            ans = None
            for (k, v) in choices.iteritems():
                if not v:
                    if total + k >= desiredTotal:
                        self.best = min(self.best, deep)
                        # print "[{}]: at sgn {}, total {} + k {} OK".format(deep, sgn, total, k)
                    else:
                        # print "[{}]: at sgn {}, total {} + k {} NOT OK".format(deep, sgn, total, k)
                        choices[k] = 1

                        child_alpha, child_beta = dfs(-sgn, choices, total + k, alpha, beta, deep + 1)

                        alpha = max(alpha, child_alpha)
                        beta = min(beta, child_beta)

                        if beta < alpha:
                            # Cut!!
                            break

                        choices[k] = 0

            return alpha, beta

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        elif maxChoosableInteger >= desiredTotal:
            return True

        self.best = maxChoosableInteger
        inf = 5555555555
        choices = {k:0 for k in xrange(1, maxChoosableInteger + 1) }
        dfs(1, choices, 0, -inf, inf, 1)
        print "best", self.best
        return True if self.best % 2 == 1 else False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        d = {}
        def dfs(sgn, choices, total, alpha, beta, deep):
            ans = False

            if choices in d:
                return d[choices]

            for bi in xrange(maxChoosableInteger):
                k = bi + 1
                v = getbit(choices, bi)
                if not v:
                    if total + k >= desiredTotal:
                        ans = True
                        break
                    else:
                        child_ans, child_alpha, child_beta = dfs(-sgn, setbit(choices, bi), total + k, alpha, beta, deep + 1)

                        if child_ans == False:
                            ans = True
                            break

                        alpha = max(alpha, child_alpha)
                        beta = min(beta, child_beta)

                        # if beta < alpha:
                        #     # Cut!!
                        #     ans = child_ans
                        #     break

            if not choices in d:
                d[choices] = (ans, alpha, beta)
            return ans, alpha, beta

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        elif maxChoosableInteger >= desiredTotal:
            return True

        inf = 5555555555
        choices = 0
        return dfs(1, choices, 0, -inf, inf, 1)[0]


sln = Solution()
print sln.canIWin(2, 1) # T
print sln.canIWin(2, 3) # F
print sln.canIWin(3, 4) # F
print sln.canIWin(10, 11) # F
print sln.canIWin(10, 40) # F
print sln.canIWin(18, 79) # T
print sln.canIWin(18, 171) # F
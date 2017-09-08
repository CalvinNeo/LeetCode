class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def fac(n):
            ans = 1
            for i in xrange(2, n + 1):
                ans *= i
            return ans
        k -= 1 # since 0
        ans = []
        vis = [False] * (n + 1)
        for i in xrange(n, 0, -1):
            base = fac(i - 1)
            pos = k / base
            print "i %d, k %d, base %d, pos %d" % (i, k, base, pos)
            kk = 0
            print vis
            for j in xrange(1, n + 1):
                if not vis[j]:
                    kk += 1
                    if kk == pos + 1:
                        vis[j] = True
                        ans.append(j)
                        break   
            k -= (base * pos)
        return ''.join(map(str, ans))

sln = Solution()
print sln.getPermutation(3, 4)
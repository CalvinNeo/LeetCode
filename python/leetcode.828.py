class Solution(object):
    def uniqueLetterStringWA(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        d = {}
        l = 0
        r = 0

        ans = 0
        def compute(length):
            tot = 0
            for i in xrange(1, length + 1):
                tot += i * (length + 1 - i)
            return tot

        def compute2(length, old_i, l, r):
            st = 1
            ed = r - old_i
            tot = (st + ed) * ed / 2
            # print "tot1", tot
            st = r - old_i - 1
            ed = st + (old_i - l)
            tot += (st + ed) * (old_i - l + 1) / 2
            # print st, ed
            # print "tot2", tot
            return tot

        flag = 0
        r_ext = 0
        while r < n:
            x = S[r]
            if not x in d:
                d[x] = r
                r += 1
                r_ext = 1
                flag = 0
            else:
                delta = len(d.keys())
                ans += compute(delta) - flag
                flag = 1
                # print "ans1", ans

                old_i = d[x]
                # print "old_i {} l {} r {}".format(old_i, l, r)
                ans += compute2(delta, old_i, l, r)
                # print "ans2", ans
                d[x] = r
                while l < r:
                    del d[S[l]]
                    l += 1

                d[x] = r
                l = r
                r += 1
                r_ext = 0

        # print l, r
        if r_ext:
            delta = len(d.keys())
            ans += compute(delta)
        return ans

    def uniqueLetterStringWA2(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        d = {}
        l = 0
        r = 0

        ans = 0
        def compute(l, r):
            st = 1
            ll = r - l + 1
            ed = st + ll - 1
            return (st + ed) * ll / 2

        def compute2(old_i, l, r):
            st = 1
            ed = r - old_i
            tot1 = (st + ed) * ed / 2
            # print "tot1", tot1
            st = r - old_i - 1
            ed = st + (old_i - l)
            tot2 = (st + ed) * (old_i - l + 1) / 2
            # print st, ed
            # print "tot2", tot2
            return tot1 + tot2

        while r < n:
            x = S[r]
            if x in d:
                old_i = d[x]
                delta = compute2(old_i, l, r)
                print "cond1[{},{}] {} old_i {}".format(l, r, delta, old_i)
                ans += delta
                while l <= old_i:
                    if S[l] in d:
                        del d[S[l]]
                    l += 1
                r += 1
                l = r
            else:
                d[x] = r
                delta = compute(l, r)
                print "cond2[{},{}] {}".format(l, r, delta)
                ans += delta
                r += 1
        return ans

    def uniqueLetterStringWA3(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        recent = {}
        l = 0
        r = 0

        ans = 0

        def compute(l, r, st = 1):
            ll = r - l + 1
            ed = st + (ll - 1)
            delta = (st + ed) * ll / 2
            return delta

        while r < n:
            x = S[r]
            if x in recent:
                i = recent[x]
                delta = compute(i + 1, r)
                delta2 = compute(0, i, r - i - 1)
                print "HAVE {} {}, [{}, {}]".format(delta, delta2, i + 1, r)
                ans += delta
                ans += delta2
            else:
                delta = compute(0, r)
                print "NO HAVE {}, [0, {}]".format(delta, r)
                ans += delta
            recent[x] = r
            r += 1
        return ans

    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        recent = {}
        l = 0
        r = 0

        ans = 0

        def compute(l, r, st = 1):
            if l > r:
                return 0
            return r - l + 1

        for i, x in enumerate(S):
            if not x in recent:
                recent[x] = []
            recent[x].append(i)

        for x, lst in recent.iteritems():
            m = len(lst)
            delta = 0
            for j in xrange(m):
                l = -1
                r = n
                if j + 1 < m:
                    r = lst[j + 1]
                if j - 1 >= 0:
                    l = lst[j - 1]

                delta = (lst[j] - l) * (r - lst[j])
                ans += delta
        return ans

# sln = Solution()
# print sln.uniqueLetterString("") # 0
# print sln.uniqueLetterString("A") # 1
# print sln.uniqueLetterString("AB") # 4
# print sln.uniqueLetterString("ABA") # 8
# print sln.uniqueLetterString("ABC") # 10
# print sln.uniqueLetterString("AAAA") # 4
# print sln.uniqueLetterString("ABAB") # 12
# print sln.uniqueLetterString("AAA") # 3
# print sln.uniqueLetterString("ABABAB") # 20
# print sln.uniqueLetterString("BABABBABAA") # 35
# print sln.uniqueLetterString("BBABAA") # 18

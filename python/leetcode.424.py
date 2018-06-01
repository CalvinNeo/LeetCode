class Solution(object):
    def characterReplacementTLE(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        mm = 0
        for i in xrange(n):
            for lk in xrange(k + 1):
                olk = lk
                rk = k - lk
                j = i
                while True:
                    while j >= 0 and s[j] == s[i]:
                        j -= 1
                    if lk and j >= 0:
                        lk -= 1
                        j -= 1
                    else:
                        break
                while j >= 0 and s[j] == s[i]:
                    j -= 1
                lb = j

                j = i
                while True:
                    while j < n and s[j] == s[i]:
                        j += 1
                    if rk and j < n:
                        rk -= 1
                        j += 1
                    else:
                        break
                while j < n and s[j] == s[i]:
                    j += 1
                rb = j
                # print "i {} lk {} rk {} [{}, {}] len {}".format(i, olk, k - olk, lb, rb, rb - lb - 1)
                mm = max(mm, rb - lb - 1)
        return mm

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        i = 0
        lst = []
        while i < n:
            x = s[i]
            j = i
            while j < n:
                if s[j] == x:
                    j += 1
                else:
                    break
            lst.append((x, j - i))
            i = j

        m = len(lst)
        ans = 0
        for i in xrange(m):
            for lk in xrange(k + 1):
                rk = k - lk
                # print "compute i = {} lk = {} rk = {}".format(i, lk, rk)
                x = lst[i][0]

                pans = lst[i][1]
                for j in xrange(i - 1, -1, -1):
                    if lst[j][0] != x:
                        if lk == 0:
                            break
                        if lk > lst[j][1]:
                            lk -= lst[j][1]
                            pans += lst[j][1]
                        else:
                            pans += lk
                            lk = 0
                            break
                    else:
                        pans += lst[j][1]

                # print "pans1", pans
                for j in xrange(i + 1, m, 1):
                    if lst[j][0] != x:
                        if rk == 0:
                            break
                        if rk > lst[j][1]:
                            rk -= lst[j][1]
                            pans += lst[j][1]
                        else:
                            pans += rk
                            rk = 0
                    else:
                        pans += lst[j][1]

                # print "pans", pans
                ans = max(ans, pans)

        return ans

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        l = 1
        r = n
        import operator
        def check1(length):
            for i in xrange(n - length + 1):
                L = s[i:i+length]
                max_cnt = max(L.count(x) for x in set(L))
                # print "Check", L, "max_cnt", max_cnt, max_cnt + k >= length
                if max_cnt + k >= length:
                    return True                    
            return False

        def check(length):
            d = {c: s[0:length].count(c) for c in s[0:length]}
            if d == {}:
                return length == 0
            if max(d.iteritems(), key=operator.itemgetter(1))[1] + k >= length:
                return True
            for i in xrange(1, n - length + 1):
                removed = s[i - 1]
                d[removed] -= 1
                inserted = s[i + length - 1]
                if inserted in d:
                    d[inserted] += 1
                else:
                    d[inserted] = 1
                if max(d.iteritems(), key=operator.itemgetter(1))[1] + k >= length:
                    return True
            return False


        while l < r:
            mi = (l + r) / 2
            flag = 0
            # print "test", mi
            if check(mi):
                # print "Suc"
                l = mi + 1
            else:
                # print "Fail"
                r = mi - 1

        # print "l", l
        if check(l):
            return l
        else:
            return l - 1


    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import operator
        n = len(s)
        if n == 0:
            return 0

        l = 0
        r = 0
        d = {}
        mm = 0
        overhead = 0
        while r < n:
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1
            while l < r:
                maj = max(d.iteritems(), key=operator.itemgetter(1))
                maj_item, maj_n = maj
                rang = r - l + 1
                overhead = rang - maj_n
                if overhead > k:
                    # shrink
                    d[s[l]] -= 1
                    l += 1
                else:
                    mm = max(mm, rang)
                    break
            r += 1
        return mm

sln = Solution()
print sln.characterReplacement("", 1) # 0
print sln.characterReplacement("ABAA", 0) # 2
print sln.characterReplacement("AAAA", 0) # 4
print sln.characterReplacement("AAAA", 2) # 4
print sln.characterReplacement("ABAB", 2) # 4
print sln.characterReplacement("AABABBA", 1) # 4
print sln.characterReplacement("ABBB", 2) # 4
print sln.characterReplacement("AAAB", 0) # 3
print sln.characterReplacement("BAAAB", 2) # 5

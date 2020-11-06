#coding: utf8

from collections import Counter
import string

class Solution(object):
    def numTilePossibilitiesTLE(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        ans = 0
        c_tot = dict(Counter(tiles))
        cs = set(tiles)

        def new_tile(s):
            c_cur = dict(Counter(s))
            newcs = set([])
            for (ch, cnt) in c_tot.iteritems():
                if ch not in c_cur or c_cur[ch] < c_tot[ch]:
                    # 新的字符ch可以加在不同的位置
                    for i in xrange(len(s) - 1):
                        ns = s[:i] + ch + s[i:]
                        # print "ns", ns
                        newcs.add(ns)
                    newcs.add(s + ch)
            return newcs

        for i in xrange(len(tiles)):
            newcs = set([])
            # print "==============", cs
            ans += len(cs)
            # 从一个长度为n的串构建一个长度为n+1的串
            for s in cs:
                # print "s", s
                ns = new_tile(s)
                newcs = newcs | ns
                # print "ns", ns
            cs = newcs

        return ans

    def numTilePossibilitiesWA(self, tiles):
        d = {}

        def fac(x):
            ans = 1
            for i in xrange(1, x + 1):
                ans *= i
            return ans

        def compute(s):
            # if s in d:
            #     return d[s]
            if s == "":
                return 0

            lst = map(int, s)
            ans = fac(sum(lst))
            for i in lst:
                ans /= fac(i)
            for i in xrange(len(lst)):
                # If I decrese one apperence
                lst[i] -= 1
                news = sorted(lst)
                news = ''.join(map(str, lst))
                news = news.replace("0", "")
                ans += compute(news)
                lst[i] += 1

            # d[s] = ans

            return ans

        c = dict(Counter(tiles))
        news = ''.join(map(str, sorted(c.values())))
        ans = compute(news)
        print d
        return ans

    def numTilePossibilities(self, tiles):
        c = dict(Counter(tiles))
        self.ans = 0
        AB = string.ascii_uppercase
        def dfs():
            for ch in AB:
                if ch in c and c[ch] > 0:
                    self.ans += 1
                    c[ch] -= 1
                    dfs()
                    c[ch] += 1
        dfs()
        return self.ans

sln = Solution()
print sln.numTilePossibilities("AAB") # 8
print sln.numTilePossibilities("AAABBC") # 188
print sln.numTilePossibilities("TBAKNLM")
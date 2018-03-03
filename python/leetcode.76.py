class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cd = {}
        length = len(s)
        target = 0
        for c in t:
            if cd.has_key(c):
                cd[c] += 1
            else:
                cd[c] = 1
                target += 1
        d = {x : 0 for x in cd.keys()}
        import sys
        inf = sys.maxint
        res = ""
        minlen = inf
        tt = 0
        l = 0
        for r in xrange(length):
            # print "--------------- l = %d, r = %d -------------------"  % (l, r)
            ch = s[r]
            if cd.has_key(ch):
                d[ch] += 1
                if d[ch] == cd[ch]:
                    tt += 1
                # print "target", target, tt
                # print "d", d, "cd", cd
                if tt >= target:
                    # print "prev (l, r) = (%d, %d)" % (l, r)
                    i = l
                    while i <= r:
                        if tt < target:
                            break
                        if cd.has_key(s[i]):
                            if d[s[i]] - 1 < cd[s[i]]:
                                break
                            else:
                                d[s[i]] -= 1
                        i += 1
                        # print "l move forward to %d, r is %d" % (i, r)
                    l = i
                    # print "(l, r) = (%d, %d), i %d, len %d, minlen %d" % (l, r, i, r - l + 1, minlen)
                    if r - l + 1 < minlen:
                        minlen = r - l + 1
                        res = s[l:r+1]
        return res



sln = Solution()
print sln.minWindow("ADOBECODEBANC", "ABC")
print sln.minWindow("A", "B")
print sln.minWindow("B", "B")
print sln.minWindow("AAA", "AA")
print sln.minWindow("ABBAA", "BA")
print sln.minWindow("BBA", "AB")
            

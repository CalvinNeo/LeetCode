class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i in xrange(len(s)):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j < len(t):
                j += 1
            else:
                return False
        return True

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c = {}
        for s in strs:
            if s not in c:
                c[s] = 1
            else:
                c[s] += 1
        l = []
        for k, v in c.iteritems():
            if v == 1:
                l.append((k, len(k), True))
            else:
                l.append((k, len(k), False))
        l.sort(key = lambda x: x[1])
        n = len(l)
        # print l
        for i in xrange(n - 1, -1, -1):
            s, length, ok = l[i]
            flag = ok
            if not flag:
                continue
            # print "handle", s
            for j in xrange(n - 1, -1, -1):
                s2, l2, ok2 = l[j]
                if i == j:
                    continue
                if self.isSubsequence(s, s2):
                    # print "conflict {} ans {}".format(s, s2)
                    flag = False
                    break
            # print "s {} flag {}".format(s, flag)
            if flag:
                return length

        return -1

sln = Solution()
print sln.findLUSlength(["aabbcc", "aabbcc","c","e","aabbcd"]) # 6
print sln.findLUSlength(["aba","cdc","eae"]) # 3
print sln.findLUSlength(["aaa","aaa","aa"]) # -1
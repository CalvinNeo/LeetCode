class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False

        def check1():
            d = {}
            for i in xrange(n):
                x = s[i]
                y = t[i]
                if not x in d:
                    d[x] = y
                else:
                    if d[x] != y:
                        return False
            return True

        def check2():
            d = {}
            for i in xrange(n):
                x = s[i]
                y = t[i]
                if not y in d:
                    d[y] = x
                else:
                    if d[y] != x:
                        return False
            return True

        return check1() and check2()

sln = Solution()
print sln.isIsomorphic("ab", "ab")
print sln.isIsomorphic("aa", "ab")
print sln.isIsomorphic("ab", "aa")
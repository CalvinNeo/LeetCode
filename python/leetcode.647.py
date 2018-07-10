class Solution(object):
    def countSubstringsW(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        stk = []
        ans = 0
        for i in xrange(n):
            stk = []
            ans += 1
            for j in xrange(i, n):
                x = s[j]
                if len(stk) == 0 or stk[-1] != x:
                    stk.append(x)
                else:
                    stk.pop(-1)
                    if len(stk) == 0:
                        ans += 1
            print "ans", ans
        return ans

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        nn = len(s)
        a = '#'.join(s)
        n = len(a)
        ans = 0
        for i in xrange(n):
            l = 0
            while 1:
                if i+l >= n or i-l < 0:
                    break
                # print "test {}".format(a[i-l:i+l+1])
                if a[i+l] == a[i-l]:
                    if a[i+l] != '#':
                        # print "add {}".format(a[i-l:i+l+1])
                        ans += 1
                else:
                    break
                l += 1
        return ans

# sln = Solution()
# print sln.countSubstrings("abc") # 3
# print sln.countSubstrings("aaa") # 6
# print sln.countSubstrings("a") # 1
# print sln.countSubstrings("aa") # 3
# print sln.countSubstrings("") # 0
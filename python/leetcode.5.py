class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def valid(x):
            return (x >= 0 and x < l)
        def makevalid(x):
            if x < 0:
                x = 0
            elif x >= l:
                x = l - 1
            return x
        def bf(x, r):
            while True:
                netr = max(0, (r - 1))
                if not (valid(x - netr) and valid(x + netr) and s[x - netr] == s[x + netr]):
                    r -= 1
                    break
                else:
                    r += 1
            return r
        s = '#' + '#'.join(s) + '#'
        # print s
        l = len(s)
        R = [1] * l
        p = 0
        for i in xrange(l):
            max_border = makevalid(p + R[p])
            # print "============="
            # print "i = %d, p = %d, R[p] = %d, max_border = %d, current char = %c" % (i, p, R[p], max_border, s[i])
            # print "S: %s" % list(s)
            # print "R : %s" % str(R)
            if i >= max_border:
                R[i] = bf(i, 1)
                # print "R[i] is %d" % (R[i])
            else:
                j = 2 * p - i
                # print "j %d" % j
                bj = j + R[j] # will not be out of range
                # print "bj %d" % bj
                if bj > p:
                    R[i] = bf(i, 2 * R[j] - R[p] + j - p)
                else:
                    R[i] = bf(i, R[j]) # Modified
            if makevalid(i + R[i]) > max_border:
                p = i
        maxi, maxr = max(zip(range(l), R), key = lambda x: x[1])
        maxlen = 2 * maxr - 1
        # print "+++++++++++++++++"
        # print maxi, maxr
        # print R
        return s[maxi - maxr + 1: maxi + maxr].replace('#', '')
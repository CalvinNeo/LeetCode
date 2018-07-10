class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        n = len(d)
        d.sort()
        inf = 55555555
        mindist = inf
        minstr = ""
        for i, x in enumerate(d):
            k1 = 0
            l1 = len(s)
            l2 = len(x)
            if l2 > l1:
                continue
            flag = 1
            for k2 in xrange(l2):
                while k1 < l1 and x[k2] != s[k1]:
                    k1 += 1
                if k1 == l1:
                    flag = 0
                    break
                else:
                    # find x[k2] == s[k1]
                    k1 += 1
            if flag:
                newdist = l1 - l2
                if newdist < mindist:
                    minstr = x
                    mindist = newdist
        return minstr
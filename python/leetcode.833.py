class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        Z = zip(indexes, sources, targets)
        ZS = sorted(Z, key = lambda x: x[0])
        indexes, sources, targets = zip(*ZS)

        # print ZS
        # print indexes
        # print sources
        # print targets

        R = ""
        cur = 0
        L = len(indexes)
        for i in xrange(L):
            if indexes[i] - cur > 0:
                R += S[cur: indexes[i]]
            # print "i {} append [{},{}] {} indexes[i] {} cur {}".format(i, cur, indexes[i], S[cur: indexes[i]], indexes[i], cur)
            cur = indexes[i]
            if S[cur: cur+len(sources[i])] == sources[i]:
                R += targets[i]
                cur += len(sources[i])
        if len(S) - cur > 0:
            R += S[cur:]

        return R

sln = Solution()

print sln.findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"])
print sln.findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"])
print sln.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"])
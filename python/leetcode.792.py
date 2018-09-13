class Solution(object):
    def numMatchingSubseqTLE(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        ll = len(S)
        dp = {}

        def is_sub(X, Y):
            # X is pattern, Y is string
            i = 0
            j = 0
            nx = len(X)
            ny = len(Y)
            if nx > ny:
                return False
            while i < nx and j < ny:
                if X[i] == Y[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == nx:
                return True
            return False

        ans = 0
        for w in words:
            if w in dp:
                ans += dp[w]
                continue
            if is_sub(w, S):
                ans += 1
                dp[w] = 1
            else:
                dp[w] = 0
        return ans

    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        ll = len(S)

        lst = [[] for i in xrange(26)]

        for i in xrange(n):
            w = words[i]
            c = w[0]
            ci = ord(c) - ord('a')
            lst[ci].append(w)

        ans = 0

        # print lst[:5]
        for i in xrange(ll):
            c = S[i]
            ci = ord(c) - ord('a')
            cur_last = len(lst[ci])
            for j in xrange(cur_last):
                w = lst[ci][j]
                if len(w) == 1:
                    # print "Add {}".format(w)
                    ans += 1
                else:
                    cc = w[1]
                    cci = ord(cc) - ord('a')
                    lst[cci].append(w[1:])
            del lst[ci][:cur_last]
            # print lst[:5]
        return ans

# sln = Solution()
# print sln.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
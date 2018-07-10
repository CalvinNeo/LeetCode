class Solution(object):
    def findSubstringTLE(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d = {}
        nn = len(words)
        if nn == 0:
            return []
        l = len(words[0])
        for w in words:
            if not w in d:
                d[w] = 1
            else:
                d[w] += 1

        ans = []
        n = len(s)
        for i in xrange(n):
            used = {}
            j = i
            while j < n:
                x = s[j:j+l]
                if (x in d) and (x not in used or used[x] < d[x]):
                    if not x in used:
                        used[x] = 1
                    else:
                        used[x] += 1
                    j += l
                else:
                    break
            flag = 1
            for k, v in d.iteritems():
                if not (k in used and used[k] == v):
                    flag = 0
                    break
            if flag:
                ans.append(i)
        return ans

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d = {}
        nn = len(words)
        if nn == 0:
            return []
        l = len(words[0])
        for w in words:
            if not w in d:
                d[w] = 1
            else:
                d[w] += 1

        ans = []
        n = len(s)
        def check(used):
            for k, v in d.iteritems():
                if not (k in used and used[k] == v):
                    return False
            return True

        for i in xrange(l):
            used = {}
            st = i
            j = st
            while j < n:
                x = s[j:j+l]
                # print "current {}, st = {}, j = {}".format(x, st, j)
                if (x in d) and (x not in used or used[x] < d[x]):
                    if not x in used:
                        used[x] = 1
                    else:
                        used[x] += 1
                    if check(used):
                        ans.append(st)
                        j += l
                    else:
                        j += l
                else:
                    # Fail here
                    # print "Fail at x = {}, start str = {}, st {}, j {}".format(x, s[st:st+l], st, j)
                    if st == j:
                        st += l
                        j = st
                    else:
                        used[s[st:st+l]] -= 1
                        st += l
                        j = max(j, st)
                    continue
        return ans

# sln = Solution()
# print sln.findSubstring("barfoothefoobarman", ["foo","bar"]) # [0, 9]
# print sln.findSubstring("wordgoodstudentgoodword", ["word","student"]) # []
# print sln.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) # []
# print sln.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) # [6,9,12]
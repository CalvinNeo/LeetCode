from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0

        c = Counter(s)
        l = -1
        while l + 1 < n and c[s[l + 1]] >= k:
            l += 1
        if l == n - 1:
            return n
        left = self.longestSubstring(s[:l+1], k)
        while l + 1 < n and c[s[l + 1]] < k:
            l += 1
        if l == n - 1:
            return left
        right = self.longestSubstring(s[l+1:], k)
        return max(left, right)

    def longestSubstringWA2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0

        # fail at aaabbb

        # leftmost of x
        l = {}
        # count of x
        c = {}
        # the leftmost place where x is valid
        v = {}

        ext = {}

        for i, x in enumerate(s):
            if x not in l:
                l[x] = i
                c[x] = 1
            else:
                c[x] += 1
            if c[x] >= k:
                v[x] = i

            flag = False
            best = l[x]
            if x in v:
                flag = True
                for j in xrange(l[x], v[x]):
                    if (not s[j] in c) or (c[s[j]] < k):
                        flag = False
                        break
                    best = min(best, l[s[j]])

            if l[x] - 1 >= 0 and l[x] - 1 in ext:
                best = min(best, ext[l[x] - 1])

            if flag:
                # print "update i {} x {} [{} {}] best {}".format(i, x, l[x], v[x], best)
                ext[v[x]] = best
                ans = max(ans, v[x] - best + 1)

        return ans


    def longestSubstringWA(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0

        w = {}
        l = -1
        r = -1

        # (l, r]
        def mx():
            if len(w.values()):
                return max(w.values())
            return 0
        def mi():
            if len(w.values()):
                return min(w.values())
            return 0
        def push(r):
            x = s[r]
            if x in w:
                w[x] += 1
            else:
                w[x] = 1
        def pop(l):
            x = s[l]
            w[x] -= 1

        while r < n:
            m = mi()
            valid = m >= k
            # print "m {} [{} {}] {}".format(m, l, r, w)
            if valid:
                # print "valid [{} {}]".format(l, r)
                ans = max(ans, r - l)
            if r + 1 >= n:
                break
            r += 1
            push(r)

        while l < n - 1:
            l += 1
            pop(l)
            m = mi()
            valid = m >= k
            if valid:
                ans = max(ans, r - l)

        return ans

sln = Solution()
print sln.longestSubstring("a", 1) # 1
print sln.longestSubstring("a", 0) # 1
print sln.longestSubstring("aaabb", 3) # 3
print sln.longestSubstring("ababbc", 2) # 5
print sln.longestSubstring("bbaaacbd", 3) # 3
print sln.longestSubstring("aaabbb", 3) # 6
print sln.longestSubstring("zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee", 10) # 21

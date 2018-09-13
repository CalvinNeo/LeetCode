class Solution(object):
    def removeDuplicateLettersWA(self, s):
        """
        :type s: str
        :rtype: str
        """
        harm = {}
        benefit = {}
        n = len(s)
        vis = {}
        for i, x in enumerate(s):
            if not x in vis:
                vis[x] = 0
            vis[x] += 1

            delta = None
            j = i
            while j < n and s[j] == x:
                j += 1
            if j < n:
                delta = ord(x) - ord(s[j])

            if not x in harm:
                harm[x] = None
            if not x in benefit:
                benefit[x] = None

            if delta == None:
                # x is the last
                if harm[x] == None:
                    harm[x] = i
                benefit[x] = i
            elif delta < 0:
                # Remove x harms, we want to be the last to remove
                if harm[x] == None:
                    # If we already have one to reserve, we keep that
                    harm[x] = i
            else:
                # Remove x benefits
                # We want to remove as early as possible, so reserve the last
                benefit[x] = i

        ans = ""
        print "benefit", benefit
        print "harm", harm
        # print vis
        for i, x in enumerate(s):
            if vis[x] > 1:
                rese = 0
                if benefit[x] != None and harm[x] != None:
                    rese = min(benefit[x], harm[x])
                elif benefit[x] != None:
                    rese = benefit[x]
                elif harm[x] != None:
                    rese = harm[x]
                # print "rese", x, rese
                if i == rese:
                    ans += x
            else:
                ans += x
        return ans

    def removeDuplicateLettersWA2(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        vis = {}
        for i, x in enumerate(s):
            if not x in vis:
                vis[x] = i
            else:
                oldi = vis[x]
                if s[oldi] > s[oldi + 1]:
                    vis[x] = i
                elif s[oldi] < s[oldi + 1]:
                    # Do not replace
                    pass
                else:
                    # The same character, do nothing
                    pass

        print list(vis.iteritems())
        lst = sorted(list(vis.iteritems()), key = lambda x:x[1])
        return ''.join([x[0] for x in lst])

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = {}
        vis = {}
        for i, x in enumerate(s):
            if not x in res:
                res[x] = 0
            res[x] += 1
            vis[x] = 0

        ans = []
        for i, x in enumerate(s):
            if not vis[x]:
                if ans:
                    while ans and x < ans[-1] and res[ans[-1]] > 0:
                        vis[ans[-1]] = 0
                        ans.pop()
                    ans.append(x)
                else:
                    ans.append(x)
            res[x] -= 1
            vis[x] = 1

        return ''.join(ans)

# sln = Solution()
# print sln.removeDuplicateLetters("") # 
# print sln.removeDuplicateLetters("abac") # abc
# print sln.removeDuplicateLetters("aab") # ab
# print sln.removeDuplicateLetters("bbaa") # ba
# print sln.removeDuplicateLetters("abba") # ab
# print sln.removeDuplicateLetters("bcabc") # abc
# print sln.removeDuplicateLetters("cbacdcbc") # acdb
# print sln.removeDuplicateLetters("abacb") # abc
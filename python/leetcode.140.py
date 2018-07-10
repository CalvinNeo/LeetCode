class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        l = len(s)
        n = len(wordDict)

        dp = [None for i in xrange(l)]
        def dfs(pos):
            if dp[pos] != None:
                return dp[pos]
            choice = []
            for i, w in enumerate(wordDict):
                ll = len(w)
                # print "now {}, try {}".format(pos, w)
                if s[pos:pos+ll] == w:
                    if pos + ll == l:
                        # print "at {}, add '{}', OK {}".format(pos, w, str(prev))
                        choice.append(w)
                    elif pos + ll < l:
                        lch = dfs(pos + ll)
                        for c in lch:
                            choice.append(w + " " + c)
            dp[pos] = choice
            return dp[pos]
        ans = dfs(0)
        # print dp
        return ans


# sln = Solution()
# print sln.wordBreak("leetcode", ["leet", "code"]) # ['leet code']
# print sln.wordBreak("applepenapple", ["apple", "pen"]) # ['apple pen apple']
# print sln.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) # []
# print sln.wordBreak("catsandog", []) # []
# print sln.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) # ['cat sand dog', 'cats and dog']
# print sln.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]) # ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']

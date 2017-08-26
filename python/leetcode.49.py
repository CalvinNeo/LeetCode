class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            pat = ''.join(sorted(list(s)))
            if d.has_key(pat):
                d[pat].append(s)
            else:
                d[pat] = [s]
        ans = []
        for (k, v) in d.iteritems():
            ans.append(v)
        return ans

sln = Solution()
print sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
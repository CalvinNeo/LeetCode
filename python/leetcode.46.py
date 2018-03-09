class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(l, c):
            if c == []:
                ans.append(l)
            for i in xrange(len(c)):
                newl = l + [c[i]]
                newc = c[:i] + c[i+1:]
                if newc == []:
                    ans.append(newl)
                else:
                    dfs(newl, newc)
        dfs([], nums)
        return ans
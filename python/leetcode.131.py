class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [None for i in xrange(n)]
        def dfs(i):
            j = i
            possible = []
            if i == n - 1:
                return [[s[i]]]
            if i >= n:
                return None
            while j < n:
                if s[i:j+1] == s[i:j+1][::-1]:
                    # print i, s[i:j+1]
                    later = dfs(j + 1)
                    if later == []:
                        pass
                    elif later == None:
                        possible.append([s[i:j+1]])
                    else:
                        possible.extend(map(lambda l: [s[i:j+1]] + l, later))
                j += 1
            return possible
        return dfs(0)

sln = Solution()
print sln.partition("aab")
print sln.partition("aba")
print sln.partition("a")
print sln.partition("abcbaa")
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        fa = range(n)
        cnt = [1] * n
        d = {nums[i]: i for i in xrange(n)}
        def find(v):
            if fa[v] == v:
                return v
            else:
                return find(fa[v])

        ans = 1
        def merge(a, b):
            aa = find(a)
            bb = find(b)
            if aa != bb:
                fa[aa] = bb
                # print "merge {} {}".format(a, b)
                cnt[bb] += cnt[aa]
            return cnt[bb]

        for (i, x) in enumerate(nums):
            if x + 1 in d:
                a = d[x]
                b = d[x + 1]
                t = merge(a, b)
                ans = max(t, ans)
            # if x - 1 in d:
            #     b = d[x - 1]
            #     a = d[x]
            #     t = merge(a, b)
            #     ans = max(t, ans)
        return ans

sln = Solution()
print sln.longestConsecutive([100, 4, 200, 1, 3, 2]) # 4
print sln.longestConsecutive([100, 4, 200, 1, 3, 300, 301, 302, 2]) # 4
print sln.longestConsecutive([100, 3]) # 1
print sln.longestConsecutive([100, 100]) # 1
print sln.longestConsecutive([100]) # 1
print sln.longestConsecutive([100, 101]) # 2
print sln.longestConsecutive([1,2,0,1]) # 3

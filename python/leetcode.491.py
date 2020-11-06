class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set([("", None)])
        n = len(nums)

        for i, x in enumerate(nums):
            ns = set(s)
            for (ys, last) in s:
                if last == None:
                    ns.add((str(x), x))
                elif x >= last:
                    ns.add((ys + "," + str(x), x))
            s = ns

        ans = []
        for ys, last in s:
            lst = ys.split(",")
            if len(lst) > 1:
                ans.append(map(int, lst))
        return ans

    def findSubsequencesWA(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        cur = []
        ans = []
        nxt = {}
        def dfs(i):
            if i >= n:
                if len(cur) >= 2:
                    ans.append(list(cur))
                return

            m = len(cur)
            x = nums[i]

            # Do not add
            dfs(i + 1)
            # Add if we can
            if not cur:
                cur.append(x)
                dfs(i + 1)
                cur.pop()
            elif x >= cur[-1]:
                key = (cur[-1], len(cur))
                if not key in nxt:
                    nxt[key] = set()
                if (x not in nxt[key]) or x == cur[-1]:
                    nxt[key].add(x)
                    cur.append(x)
                    dfs(i + 1)
                    cur.pop()
        dfs(0)
        print nxt
        return ans

sln = Solution()
print sln.findSubsequences([4, 6, 7, 7])
print sln.findSubsequences([4])
print sln.findSubsequences([])
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        length = len(candidates)
        ans = []
        def dfs(current_sum, i, vis):
            if current_sum == target:
                pairs = filter(lambda x: x[0] > 0, zip(vis, candidates))
                newans = []
                for kv in pairs:
                    y = [kv[1]] * kv[0]
                    newans.extend(y)
                ans.append(newans)
                return
            if i >= length:
                return
            nvis = (target - current_sum) / candidates[i] + 1
            newvis = vis + [0] # IMPORTANT: create new vis array
            for newvis[i] in xrange(0, nvis + 1):
                tot = current_sum + candidates[i] * newvis[i]
                if i < length and tot <= target:
                    dfs(tot, i + 1, newvis)

        dfs(0, 0, [])
        return ans

sln = Solution()
print sln.combinationSum([2,3,6,7], 7)

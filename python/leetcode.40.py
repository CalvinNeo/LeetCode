class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        mm = {}
        for x in candidates:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        cans = []
        for (k,v) in mm.items():
            cans.append(k)
        length = len(cans)
        ans = []
        def dfs(current_sum, i, vis):
            if current_sum == target:
                pairs = filter(lambda x: x[0] > 0, zip(vis, cans))
                newans = []
                for kv in pairs:
                    y = [kv[1]] * kv[0]
                    newans.extend(y)
                ans.append(newans)
                return
            if i >= length:
                return
            nvis = mm[cans[i]] 
            newvis = vis + [0] # IMPORTANT: create new vis array
            for newvis[i] in xrange(0, nvis + 1):
                tot = current_sum + cans[i] * newvis[i]
                if i < length and tot <= target:
                    dfs(tot, i + 1, newvis)

        dfs(0, 0, [])
        return ans
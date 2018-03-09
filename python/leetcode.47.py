class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        ans = []
        d = {x : nums.count(x) for x in nums}
        def dfs(l, c):
            if len(l) == length:
                ans.append(l)
                return
            for i in c.keys():
                if c[i] > 0:
                    newl = l + [i]
                    c[i] -= 1
                    if len(newl) == length:
                        ans.append(newl)
                    else:
                        dfs(newl, c)
                    c[i] += 1
        dfs([], d)
        return ans
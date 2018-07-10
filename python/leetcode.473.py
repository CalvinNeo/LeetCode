def setbit(x, i):
    return (x | (1 << i)) & 0xffffffff

def unsetbit(x, i):
    return x & ((~(1 << i)) & 0xffffffff) & 0xffffffff

def getbit(x, i):
    return (x >> i) & 1 & 0xffffffff

class Solution(object):
    def makesquareTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:
            return False
        tot_len = sum(nums)
        av = tot_len / 4
        if av * 4 != tot_len:
            return False
        nums.sort()
        if nums[-1] > av:
            return False

        vis = [0] * n
        def dfs(cur_sum, cur_edge, vcnt):
            if cur_edge == 4:
                if cur_sum == 0 and vcnt == n:
                    return True
                else:
                    return False
            for i in xrange(n - 1, -1, -1):
                if not vis[i]:
                    nxt_sum = cur_sum + nums[i]
                    vis[i] = 1
                    if nxt_sum == av:
                        if dfs(0, cur_edge + 1, vcnt + 1):
                            return True
                    elif nxt_sum < av:
                        if dfs(nxt_sum, cur_edge, vcnt + 1):
                            return True
                    vis[i] = 0
            return False
        return dfs(0, 0, 0)

    def makesquareTLE2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:
            return False
        tot_len = sum(nums)
        av = tot_len / 4
        if av * 4 != tot_len:
            return False
        nums.sort()
        if nums[-1] > av:
            return False

        vis = [0] * n
        def dfs2(cur_sum, mode):
            if cur_sum == av:
                return True
            for i in xrange(n - 1, -1, -1):
                if vis[i] == mode:
                    nxt_sum = cur_sum + nums[i]
                    vis[i] = 2
                    if nxt_sum <= av:
                        if dfs2(nxt_sum, mode):
                            vis[i] = mode
                            return True
                    vis[i] = mode
            return False

        def dfs1(cur_sum):
            if cur_sum == av * 2:
                return dfs2(0, 0) and dfs2(0, 1)
            for i in xrange(n - 1, -1, -1):
                if not vis[i]:
                    vis[i] = 1
                    nxt_sum = cur_sum + nums[i]
                    if nxt_sum <= av * 2:
                        if dfs1(nxt_sum):
                            return True
                    vis[i] = 0
            return False

        return dfs1(0)

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:
            return False
        tot_len = sum(nums)
        av = tot_len / 4
        if av * 4 != tot_len:
            return False
        nums.sort(reverse = True)
        if nums[-1] > av:
            return False

        edge = [0] * 4
        def dfs(p):
            if p == n:
                return True
            for i in xrange(4):
                if edge[i] + nums[p] <= av:
                    edge[i] += nums[p]
                    if dfs(p + 1):
                        return True
                    edge[i] -= nums[p]
            return False

        return dfs(0)

sln = Solution()
print sln.makesquare([1,1,1,1]) # T
print sln.makesquare([1,1,2,2,2]) # T
print sln.makesquare([3,3,3,3,4]) # F
print sln.makesquare([5,4,3,5,4,3,5,4,3,5,4,3]) # T
print sln.makesquare(range(16)) # T
print sln.makesquare([1,2,1,2,3,1,1,1,1,1,1,1,4]) # T
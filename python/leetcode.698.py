def set_bit(val, i):
    val |= (1 << i)
    val &= 0xffffffff
    return val
def unset_bit(val, i):
    val &= ((~(1 << i)) & 0xffffffff)
    val &= 0xffffffff
    return val
def check_bit(val, i):
    return val & (1 << i)
class Solution(object):
    def canPartitionKSubsetsTLE_WA(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        nums.sort()
        n = len(nums)
        ss = sum(nums)
        av = ss / k
        if av * k != ss:
            return False
        MAGIC = 1000000
        def dfs(vis, cur, used):
            print vis, cur
            # if vis * MAGIC + cur in d:
            #     return d[vis * MAGIC + cur]
            if cur == av:
                used += 1
                cur = 0
            if used == k:
                d[vis * MAGIC + cur] = True
                return d[vis * MAGIC + cur]
            for i in xrange(n):
                if (not check_bit(vis, i)) and cur + nums[i] <= av:
                    vis = set_bit(vis, i)
                    if dfs(vis, cur + nums[i], used):
                        d[vis * MAGIC + cur] = True
                        return d[vis * MAGIC + cur]
                    vis = unset_bit(vis, i)
            d[vis * MAGIC + cur] = False
            return d[vis * MAGIC + cur]
        return dfs(0, 0, 0)

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        nums.sort()
        n = len(nums)
        ss = sum(nums)
        av = ss / k
        if av * k != ss:
            return False
        MAGIC = 1000000
        def dfs(vis, cur, used, deep):
            if vis * MAGIC + cur in d:
                return d[vis * MAGIC + cur]
            if cur == av:
                used += 1
                cur = 0
            if used == k:
                return True
            # print vis, cur, vis * MAGIC + cur
            for i in xrange(n):
                if (not check_bit(vis, i)) and cur + nums[i] <= av:
                    vis = set_bit(vis, i)
                    if vis * MAGIC + cur + nums[i] in d:
                        return d[vis * MAGIC + cur + nums[i]]
                    if dfs(vis, cur + nums[i], used, deep + 1):
                        return True
                    vis = unset_bit(vis, i)
            d[vis * MAGIC + cur] = False
            return d[vis * MAGIC + cur]
        return dfs(0, 0, 0, 0)
sln = Solution()
print sln.canPartitionKSubsets([1,1], 1)
print sln.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
print sln.canPartitionKSubsets([4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2], 13)
print sln.canPartitionKSubsets([4,3,2,1,3,2,5,5,5,5,5,5,5,5], 11)

# 这两种搜索的方法都不能成功运行，但用C++改写后就可以了
import sys
def dfs(deep, total, nums, l, r):
    sgn = 1 if deep % 2 == 0 else -1
    if deep == total - 1:
        return nums[l] * sgn
    ans_l = dfs(deep + 1, total, nums, l + 1, r) + nums[l] * sgn
    ans_r = dfs(deep + 1, total, nums, l, r - 1) + nums[r] * sgn
    if deep % 2 == 0:
        # MAX
        return max(ans_l, ans_r)
    else:
        # MIN
        return min(ans_l, ans_r)

def alphabeta_dfs(sgn, nums, l, r, alpha, beta):
    if l == r:
        if sgn > 0:
            return (nums[l], nums[l], sys.maxint)
        else:
            return (nums[l], -sys.maxint, -nums[l])

    (lnd, child_alpha, child_beta) = alphabeta_dfs(-sgn, nums, l + 1, r, alpha, beta)
    ansl = lnd + sgn * nums[l]
    alpha = max(alpha, child_alpha)
    beta = min(beta, child_beta)

    if beta >= alpha:
        (rnd, child_alpha, child_beta) = alphabeta_dfs(-sgn, nums, l, r - 1, alpha, beta)
        ansr = rnd + sgn * nums[r]
        alpha = max(alpha, child_alpha)
        beta = min(beta, child_beta)

        if sgn > 0:
            return (max(ansl, ansr), alpha, beta)
        else:
            return (min(ansl, ansr), alpha, beta)
    else:
        return (ansl, alpha, beta)

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # return dfs(0, n, nums, 0, n - 1) >= 0
        return alphabeta_dfs(1, nums, 0, n - 1, -sys.maxint, sys.maxint)[0] >= 0

sln = Solution()
print sln.PredictTheWinner([1])
print sln.PredictTheWinner([1, 2])
print sln.PredictTheWinner([1, 5, 2])
print sln.PredictTheWinner([1, 5, 233, 7])
print sln.PredictTheWinner(range(0, 20))
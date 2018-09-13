#coding:utf8
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # 模拟真实情况，可以贪心直接匹配
        i = 0
        n = len(row)
        ans = 0
        while i < n:
            if row[i] | 1 == row[i + 1] | 1:
                # print "Equal at {}, {} {}".format(i, row[i] | 1, row[i + 1] | 1)
                pass
            else:
                for j in xrange(i + 1, n):
                    if row[i] | 1 == row[j] | 1:
                        row[i + 1], row[j] = row[j], row[i + 1]
                        ans += 1
                        break
            i += 2
        return ans

        
sln = Solution()
print sln.minSwapsCouples([0, 2, 1, 3]) # 1
print sln.minSwapsCouples([3, 2, 0, 1]) # 0
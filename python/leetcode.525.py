class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        delta = 0
        n = len(nums)
        st = {0:[-1]}

        mx = 0
        acc = 0
        for i in xrange(n):
            x = nums[i]
            delta = 0
            if x == 0:
                delta -= 1
            else:
                delta += 1

            acc += delta
            wanna_find = acc
            # print "acc", acc, "Wanna find", wanna_find, wanna_find in st
            if wanna_find in st:
                # print "==>", i, st[wanna_find]
                mx = max(mx, i - min(st[wanna_find]))

            # Update
            if not acc in st:
                st[acc] = []
            st[acc].append(i)

        return mx

# sln = Solution()
# print sln.findMaxLength([0,1]) # 2
# print sln.findMaxLength([0,1,0]) # 2
# print sln.findMaxLength([0,1,1]) # 2
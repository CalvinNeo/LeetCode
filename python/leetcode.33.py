class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1
        def bs(l, r, x):
            if l == r:
                if x == nums[l]:
                    return l
                else:
                    return -1
            elif l > r:
                return -1
            m = (l + r) / 2
            if nums[m] > x:
                return bs(l, m - 1, x)
            elif nums[m] == x:
                return m
            else:
                return bs(m + 1, r, x)

        def bs2(l, r):
            m = (l + r) / 2
            # print "l %d r %d m %d, nums[m] %d nums[l] %d" % (l, r, m, nums[m], nums[l])
            if l + 1 >= r:
                # print "hit 1"
                if nums[l] > nums[r]:
                    return l
                else:
                    return r
            if m >= length and nums[m] > nums[m + 1]:
                # print "hit 2"
                return m
            elif nums[m] >= nums[l]:
                # print "hit 3"
                return bs2(m, r)
            else:
                # print "hit 4"
                return bs2(l, m - 1)

        piv = bs2(0, length - 1)
        ans1 = bs(0, piv, target)
        ans2 = bs(piv + 1, length - 1, target)
        return ans2 if ans1 == -1 else ans1
class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        l = [0]
        for x in differences:
            l.append(l[-1] + x)

        mi = min(l)
        mx = max(l)


        ai = lower - mi
        ax = upper - mx

        ans = ax - ai + 1
        return 0 if ans < 0 else ans

s = Solution()
print (s.numberOfArrays([1,-3,4], 1, 6))
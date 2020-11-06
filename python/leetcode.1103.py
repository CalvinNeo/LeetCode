class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        n = candies
        t = 0.5 * ((8 * n + 1) ** 0.5 - 1)
        t = int(t)
        # t = 0 1 1 2 2 2 3 3 3 3 4 4 4 4 4
        rest = n - (1 + t) * t / 2 # Rest candies
        ans = [0] * num_people
        r = int(t / num_people) # How many round
        rest_r = t - r * num_people # How many people in last round which get full candy
        # print "t", t, "rest", rest, 'r', r, 'rest_r', rest_r
        for i in xrange(num_people):
            ans[i] = r * (r - 1) * num_people / 2 + (i + 1) * r
            # print "origin ans[{}] = {}".format(i, ans[i])
            if i == rest_r:
                ans[i] += rest
            elif i < rest_r:
                ans[i] += r * num_people + (i + 1)
        return ans
        
sln = Solution()
print sln.distributeCandies(7, 4) # 1 2 3 1
print sln.distributeCandies(10, 3) # 5 2 3

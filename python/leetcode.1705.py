class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        ans = 0
        n = len(apples)
        last = 0 # on this day, we have no apple to eat
        for i, (a, d) in enumerate(zip(apples, days)):
            if i <= last:
                # print("eat at {}".format(i))
                ans += 1
            if min(a, d) > 0:
                last = max(last, i + min(a, d))
            # print("last {}".format(last))

        if last > n:
             ans += last - n
        return ans

s = Solution()
# print (s.eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]))
print (s.eatenApples(apples = [2,1,10], days = [2,10,1])) # 4

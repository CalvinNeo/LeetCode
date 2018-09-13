class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)

        d = {5:0, 10:0, 20:0}

        for i, x in enumerate(bills):
            d[x] += 1
            if x == 20:
                if d[10] > 0:
                    d[10] -= 1
                    d[5] -= 1
                else:
                    d[5] -= 3
            elif x == 10:
                d[5] -= 1
            if d[5] < 0:
                return False
        return True

# sln = Solution()
# # t t f f
# print sln.lemonadeChange([5,5,5,10,20])
# print sln.lemonadeChange([5,5,10])
# print sln.lemonadeChange([10,10])
# print sln.lemonadeChange([5,5,10,10,20])

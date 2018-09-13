class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)
        def hash_list(lst):
            ans = 0
            for x in lst:
                ans += x
                ans *= 7

        d = {}

        def dfs(rest):
            # Simple buy
            inf = 555555555555
            tot = 0

            for i, x in enumerate(rest):
                if x < 0:
                    return inf

            key = hash_list(rest)
            # if key in d:
            #     return d[key]

            for i, x in enumerate(rest):
                tot += x * price[i]

            n_offer = len(special)
            for j in xrange(n_offer):
                delta = special[j][-1]
                for i in xrange(n):
                    rest[i] -= special[j][i]

                par = dfs(rest) + delta
                tot = min(par, tot)

                for i in xrange(n):
                    rest[i] += special[j][i]

            d[key] = tot
            return tot

        return dfs(needs)

# sln = Solution()
# print sln.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2])
# print sln.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])
# print sln.shoppingOffers([], [], [])
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        if n == 1:
            return 0
        s = 0
        # for (i, (g, c)) in enumerate(zip(gas, cost)):
        l, r = -1, n
        last_move = 0
        while r > l:
            while l + 1 < r:
                l += 1
                g, c = gas[l], cost[l]
                if s + g - c >= 0:
                    s += g - c
                    # print "l move to {}".format(l)
                    last_move = 0
                else:
                    l -= 1
                    break
            while r > l:
                r -= 1
                g, c = gas[r], cost[r]
                s += g - c
                last_move = 1
                # print "r move to {}".format(r)
                if s + gas[l] - cost[l] >= 0:
                    break

        return (r + 1) % n


sln = Solution()
print sln.canCompleteCircuit([4], [5]) # -1
print sln.canCompleteCircuit([1,2,3], [1,2,3]) # 0, 1, 2
print sln.canCompleteCircuit([1,2], [2,1]) # 1
print sln.canCompleteCircuit([2,3,1], [3,1,2]) # 1
print sln.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) # 3
print sln.canCompleteCircuit([2,0,1,2,3,4,0], [0,1,0,0,0,0,11]) # 0


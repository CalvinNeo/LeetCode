# coding: utf8
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations.sort()
        n = len(stations)
        current_fuel = startFuel
        current_dist = 0
        if n == 0:
            return 0 if current_fuel >= target else -1
        else:
            current_fuel -= stations[0][0]
            current_dist = stations[0][0]

        # 第i个加油站往后一共有多少油
        have = [0] * (n + 1)
        for i in xrange(n - 1, -1, -1):
            if i == n - 1:
                have[i] = stations[i][1]
            else:
                have[i] = have[i + 1] + stations[i][1]
        max_need = [0] * (n + 1)
        for i in xrange(n, -1, -1):
            if i == n:
                max_need[i] = target - stations[-1][0]
            elif i == 0:
                max_need[i] = max(max_need[i + 1], max_need[i + 1] - stations[i][1] + stations[i][0])
            else:
                max_need[i] = max(max_need[i + 1], max_need[i + 1] - stations[i][1] + stations[i][0] - stations[i - 1][0])

        ans = 0
        for i in xrange(n):
            # 在加油站i到加油站i+1
            nxt = target
            if i != n - 1:
                nxt = stations[i + 1][0]
            # print "i {}, fuel {}, dis {}, nxt {}".format(i, current_fuel, current_dist, nxt)
            if current_fuel < 0:
                return -1
            if current_fuel < nxt - current_dist:
                # print "Stop at", i
                ans += 1
                current_fuel = current_fuel - (nxt - current_dist) + stations[i][1]
                current_dist = nxt
            else:
                if current_fuel < max_need[i]:
                    # print "Stop at", i
                    ans += 1
                    current_fuel += stations[i][1]
                else:
                    current_fuel = current_fuel - (nxt - current_dist)
                    current_dist = nxt

        if current_fuel >= 0:
            return ans
        else:
            return -1

sln = Solution()
print sln.minRefuelStops(1, 1, []) # 0
print sln.minRefuelStops(100, 1, [[10, 100]]) # -1
print sln.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]) # 2
print sln.minRefuelStops(100,25,[[25,25],[50,25],[75,25]]) # 3
print sln.minRefuelStops(1000,83,[[47,220],[65,1],[98,113],[126,196],[186,218],[320,205],[686,317],[707,325],[754,104],[781,105]]) # 4
